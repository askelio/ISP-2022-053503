from cgitb import text
import json
from urllib import response
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async
from django.contrib.auth import get_user_model



class chat_consumer(AsyncConsumer):
    async def websocket_connect(self,event):
        print('connected', event)

        await self.send({
            'type': 'websocket.accept'
        })
    
    async def websocket_receive(self,event):

        received_data = json.loads(event['text'])
        msg = received_data.get('message')

        print('resived', event)

        response = {
            'message': msg
        }

        if not msg:
            return False

        await self.send({
            'type':'websocket.send',
            'text': json.dumps(response)
        })

    async def websocket_disconnect(self,event):
        print('disconnected', event)
