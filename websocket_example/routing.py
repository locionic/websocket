from django.urls import re_path
from ws_app import consumers
websocket_urlpatterns=[
    re_path(r'ws/sohoaapidev/',consumers.ChatConsumer.as_asgi())
]