from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer

from asgiref.sync import async_to_sync


class MyJsonWebsocketConsumer(JsonWebsocketConsumer):

    def connect(self):
        print('---------------Synchronous Connection Opened.---------------')
        print(self.channel_layer)
        print(self.channel_name)
        print(self.scope)
        self.group_name =  self.scope['url_route']['kwargs']['groupName']

        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()
    

    def receive_json(self, content, **kwargs):
        print('---------------Receive Dta---------------', content)

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'send.messages',
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

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()
    

    async def receive_json(self, content, **kwargs):
        print('---------------Receive Data---------------', content)

        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'send.messages',
                'text': content
            }
        )
    

    async def send_messages(self, event): # custom event handler, event is "send.messages"
        await self.send_json(event['text'])

