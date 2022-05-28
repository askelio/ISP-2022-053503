from django.urls import path

from . import consumers

websocket_urlpatterns =[
    path('chat_page/', consumers.chat_consumer.as_asgi()),
]