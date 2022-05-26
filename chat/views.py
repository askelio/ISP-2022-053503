from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'chat/index.html')


def login(request):
    return render(request, 'chat/login.html')

def register(request):
    return render(request, 'chat/register.html')