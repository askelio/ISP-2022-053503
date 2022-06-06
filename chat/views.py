
from django.shortcuts import render, redirect 



from asgiref.sync import sync_to_async

from django.contrib.auth import authenticate, login, logout

import django.contrib as djc

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from .serializers import message_serializer

from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

from rest_framework.parsers import JSONParser

import logging
logger = logging.getLogger(__name__)

# Create your views here.
from .models import *
from .forms import CreateUserForm

@sync_to_async
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

				logger.info(f'Account was created for {user}')

				return redirect('login')
        

			

		context = {'form':form}
		return render(request, 'chat/register.html', context)


@sync_to_async
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

					logger.info(f'{user} is authenticated')

					return redirect('chats')             

				else:                
					djc.messages.info(request, 'Username OR password is incorrect')
                
                

		context = {}
		return render(request, 'chat/login.html', context)

@sync_to_async
def logout_view(request):

	logger.info(f'{request.user.username} is exit')

	logout(request)
	return redirect('login')


@sync_to_async
def index(request):
    return render(request, 'chat/index.html', {})


@sync_to_async
@login_required
def delete_acc(request):
	temp = request.user.username
	User.objects.filter(username = request.user.username).exclude(is_staff = True).delete()	

	logger.info(f'{temp} account is deleted')

	return redirect('login')

	# User.objects.filter(username = request.get('username')).exclude(is_staff = True).delete()	
	# return redirect('login')


@sync_to_async
@login_required
def search_view(request, parameter):
	# return JsonResponse({"search":User.objects.filter(username = parameter)})	
	if request.method == 'GET':
		return render(request, 'chat/chat_page.html',
						{'users': User.objects.exclude(username = request.user.username).filter(username=parameter)})


@sync_to_async
@login_required
def chat_view(request):
	# a = Q(receiver = request.user.id )
	# b = Q(sender = request.user.id)
	# q = friend_request.objects.exclude(is_approved = 'False')
	# q = q.filter(a | b)
	

	return render(request, 'chat/chat_page.html',
                      {'users': User.objects.exclude(username=request.user.username)})


@sync_to_async
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


@sync_to_async
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