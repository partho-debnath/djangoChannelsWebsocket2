from django.urls import path

from . import consumers

websocket_urlpatterns = [ 
    path('ws/chat/jsc/<str:groupName>/', consumers.MyJsonWebsocketConsumer.as_asgi()),

]