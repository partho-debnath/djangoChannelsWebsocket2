from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async

from asgiref.sync import async_to_sync

from .models import Group, Chat



class MyJsonWebsocketConsumer(JsonWebsocketConsumer):

    def connect(self):
        print('---------------Synchronous Connection Opened.---------------')
        print(self.channel_layer)
        print(self.channel_name)
        print(self.scope)
        
        self.group_name =  self.scope['url_route']['kwargs']['groupName']
        self.group_obj = Group.objects.get(name=self.group_name) # get the client group name object

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    

    def receive_json(self, content, **kwargs):
        print('---------------Receive Dta---------------', content)
        
        if self.scope['user'].is_authenticated == True:
            print('Authorized User----------------: ', self.scope['user'])

            Chat.objects.create(group=self.group_obj, text=content['messages']) # save the client messages
            content['username'] = self.scope['user'].username
        else:
            print('Unauthorized User----------------: ', self.scope['user'])
            
            content = {
                'messages': 'Login Required. Before sending any message you must be login.',
                'username': 'Unauthorized User'
            }

        self.messageDealaverytoGroup(content)
    

    def messageDealaverytoGroup(self, content):     # custom function

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'send.messages',  # here "send.messages" is a custom event.
                'text': content
            }
        )


    def send_messages(self, event): # custom event handler, event is "send.messages"
        self.send_json(event['text'])



class MyAsyncJsonWebsocketConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print('---------------Asynchronous Connection Opened.---------------')
        print(self.channel_layer)
        print(self.channel_name)
        print(self.scope)

        self.group_name =  self.scope['url_route']['kwargs']['groupName']
        self.group_obj = await database_sync_to_async(Group.objects.get)(name=self.group_name) # get the client group name object

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
    

    async def receive_json(self, content, **kwargs):
        print('---------------Receive Data---------------', content)

        if self.scope['user'].is_authenticated == True:
            print('Authorized User----------------: ', self.scope['user'])

            # save the client messages
            await database_sync_to_async(Chat.objects.create)(group=self.group_obj, text=content['messages'])
            content['username'] = self.scope['user'].username
        
        else:
            print('Unauthorized User----------------: ', self.scope['user'])
            
            content = {
                'messages': 'Login Required. Before sending any message you must be login.',
                'username': 'Unauthorized User'
            }

        await self.messageDealaverytoGroup(content)


    async def messageDealaverytoGroup(self, content):     # custom function

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send.messages',  # here "send.messages" is a custom event.
                'text': content
            }
        )
    

    async def send_messages(self, event): # custom event handler, event is "send.messages"
        await self.send_json(event['text'])

