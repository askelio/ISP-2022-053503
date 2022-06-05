
import json
from django.dispatch import receiver
from django.shortcuts import render, redirect 

from django.db.models import Q


from django.contrib.auth import authenticate, login, logout

import django.contrib as djc

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from .serializers import user_serializer,message_serializer

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

from rest_framework.parsers import JSONParser


# Create your views here.
from .models import *
from .forms import CreateUserForm





def register_view(request):
	if request.user.is_authenticated:  

		return redirect('login')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				djc.messages.success(request, 'Account was created for ' + user)
				return redirect('login')
        

			

		context = {'form':form}
		return render(request, 'chat/register.html', context)

def login_view(request):
	if request.user.is_authenticated:
		return redirect('chats')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('chats')             

			else:                
				djc.messages.info(request, 'Username OR password is incorrect')
                
                

		context = {}
		return render(request, 'chat/login.html', context)

def logout_view(request):
	logout(request)
	return redirect('login')





def index(request):
    return render(request, 'chat/index.html', {})

@login_required
def search_view(request, parameter):
	# return JsonResponse({"search":User.objects.filter(username = parameter)})	
	return render(request, 'chat/chat_page.html',
                      {'users': User.objects.exclude(username = request.user.username).filter(username=parameter)})


@login_required
def chat_view(request):
	# a = Q(receiver = request.user.id )
	# b = Q(sender = request.user.id)
	# q = friend_request.objects.exclude(is_approved = 'False')
	# q = q.filter(a | b)
	

	return render(request, 'chat/chat_page.html',
                      {'users': User.objects.exclude(username=request.user.username)})

@login_required
def message_view(request, sender, receiver):
	

	if not request.user.is_authenticated:
		return redirect('index')
	if request.method == "GET":

		
		return render(request, "chat/messages.html",
					{
					'users': User.objects.exclude(username=request.user.username),
					'receiver': User.objects.get(id=receiver),
					'messages': Message.objects.filter(sender_id=sender, receiver_id=receiver) |
								Message.objects.filter(sender_id=receiver, receiver_id=sender)})


@login_required
@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = message_serializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = message_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)