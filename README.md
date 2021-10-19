# real_time_tic_tac_game_using_dajngo_and_channels

for the async call I used the django package channels.

Channels is a project that takes Django and extends its abilities beyond HTTP
- to handle WebSockets, chat protocols, IoT protocols, and more.
It’s built on a Python specification called ASGI.


I used redis:
The primary purpose of redis in django-channel_layers is to store the necessary information required
for different instances of consumers to communicate with one another.

It is clear that Redis is used as a storage layer for channel names and group names.
These are stored within Redis so that they can be accessed from any consumer instance

whenever I want to send data to the channels in the group I can simply reference the group
from my consumer and Django-channels will automatically retrieve the channel names stored under that group in Redis.
