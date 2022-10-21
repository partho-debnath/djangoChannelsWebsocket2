"""
ASGI config for djangoChannelsWebsocket2 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application

from channels.routing import ProtocolTypeRouter, URLRouter

from chat import routing as chatrouting

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoChannelsWebsocket2.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter(
            chatrouting.websocket_urlpatterns
        )
    }
)
