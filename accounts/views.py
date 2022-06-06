from django.shortcuts import render
from asgiref.sync import sync_to_async
from django.shortcuts import render, redirect 
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login

import django.contrib as djc

import logging
logger = logging.getLogger(__name__)

# Create your views here.

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
		return render(request, 'accounts/register.html', context)


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
		return render(request, 'accounts/login.html', context)