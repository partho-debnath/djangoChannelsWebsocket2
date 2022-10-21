from channels.generic.websocket import JsonWebsocketConsumer, AsyncJsonWebsocketConsumer



class MyJsonWebsocketConsumer(JsonWebsocketConsumer):

    def connect(self):
        print('---------------Synchronous Connection Opened.---------------')
        print(self.channel_layer)
        print(self.channel_name)
        print(self.scope)
        self.accept()