from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

import django.contrib as djc

from django.contrib.auth.decorators import login_required

from django.http import JsonResponse

from .serializers import user_serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User

# Create your views here.
from .models import *
from .forms import CreateUserForm

def index(request):
    return render(request, 'chat/index.html')

# @login_required
def chat_page(request):
    return render(request, 'chat/chat_page.html')


def registerPage(request):
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

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('chat_page')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('chat_page')             

			else:                
				djc.messages.info(request, 'Username OR password is incorrect')
                
                

		context = {}
		return render(request, 'chat/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


def user_request(request):
	user = User.objects.get(id=2)
	serialier = user_serializer(user, many = False)
	return JsonResponse(serialier.data, safe=False)

	
