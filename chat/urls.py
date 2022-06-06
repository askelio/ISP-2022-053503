from django.urls import path
from . import views




urlpatterns = [
    path('logout/', views.logout_view, name='logout'),

    path('chat/', views.chat_view, name='chats'),
    path('chat/<int:sender>/<int:receiver>/', views.message_view, name='chat'),
    path('api/messages/<int:sender>/<int:receiver>/', views.message_list, name='message-detail'),
    path('api/messages/', views.message_list, name='message-list'),

    path('search/<str:parameter>/', views.search_view, name='search'), 
    path('delete/', views.delete_acc, name='delete'),   
]