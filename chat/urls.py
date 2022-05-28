from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= "index"),
    path('chat_page/', views.chat_page, name= "chat_page"), 
    path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    
    path('users/', views.user_request, name="users/"),
]