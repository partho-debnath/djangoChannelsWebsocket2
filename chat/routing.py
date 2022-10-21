from django.urls import path

from . import consumers

websocket_urlpatterns = [ 
    path('ws/chat/scj/<str:groupName>/', consumers.MyJsonWebsocketConsumer.as_asgi()),
    path('ws/chat/acj/<str:groupName>/', consumers.MyAsyncJsonWebsocketConsumer.as_asgi())
]