from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
import json

class TicTacConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_code']

        # print("--------user-----:", self.scope['user'])
        # print("--------header----:", self.scope['headers'])
        # print("--------url route----:" ,self.scope["url_route"])
        # print("-----kwargs----------:", self.scope['url_route']['kwargs'])

        self.room_group_name = 'room_%s'%self.room_name
        # print("-----room_name----",self.room_group_name)

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
        self.send(text_data=json.dumps({'status':'ok'}))

    def receive(self, text_data=None, bytes_data=None):
        print(text_data)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,{
                'type':'run_game',
                'payload': text_data
            }
        )

    def disconnect(self, close_code):

        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
    
    def run_game(self,event):
        data = event['payload']
        data = json.loads(data)
        self.send(text_data = json.dumps({
            'payload':data['data']
        }))