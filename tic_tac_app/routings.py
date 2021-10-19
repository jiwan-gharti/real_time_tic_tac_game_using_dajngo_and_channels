
from django.urls import path
from tic_tac_app.consumers import TicTacConsumer

ws_urlpatterns = [
    path("ws/tic_tac/<room_code>/", TicTacConsumer.as_asgi())
]