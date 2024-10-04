# import json
# from channels.generic.websocket import AsyncWebsocketConsumer
# from datetime import datetime

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.room_name = self.scope['url_route']['kwargs']['room_name']
#         self.room_group_name = f'chat_{self.room_name}'

#         # User authentication check
#         if self.scope['user'].is_anonymous:
#             await self.close()
#         else:
#             await self.channel_layer.group_add(
#                 self.room_group_name,
#                 self.channel_name
#             )
#             await self.accept()

#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         try:
#             text_data_json = json.loads(text_data)
#             message = text_data_json.get('message')
#             typing = text_data_json.get('typing')
#             user = self.scope['user']

#             # Handle typing event if present
#             if typing is not None:
#                 await self.channel_layer.group_send(
#                     self.room_group_name,
#                     {
#                         'type': 'user_typing',
#                         'typing': typing,
#                         'sender': user.username
#                     }
#                 )

#             # Handle message if present
#             if message:
#                 timestamp = datetime.now().strftime('%H:%M:%S')
#                 await self.channel_layer.group_send(
#                     self.room_group_name,
#                     {
#                         'type': 'chat_message',
#                         'message': message,
#                         'user': user.username,
#                         'timestamp': timestamp
#                     }
#                 )

#         except json.JSONDecodeError:
#             print("Invalid JSON received")

#     async def chat_message(self, event):
#         message = event['message']
#         user = event['user']
#         timestamp = event['timestamp']

#         # Send message to WebSocket with user info and timestamp
#         await self.send(text_data=json.dumps({
#             'message': message,
#             'username': user,
#             'timestamp': timestamp,
#             'typing': False
#         }))

#     async def user_typing(self, event):
#         typing = event['typing']
#         sender_username = event['sender']

#         await self.send(text_data=json.dumps({
#             'typing': typing,
#             'username': sender_username
#         }))






#  This is final code ................................................................................












































































import json
from channels.generic.websocket import AsyncWebsocketConsumer
from datetime import datetime

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'chat_{self.room_name}'

        # User authentication check
        if self.scope['user'].is_anonymous:
            await self.close()
        else:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get('message')
            typing = text_data_json.get('typing')
            user = self.scope['user']

            # Handle typing event if present
            if typing is not None:
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'user_typing',
                        'typing': typing,
                        'sender': user.username
                    }
                )

            # Handle message if present
            if message:
                timestamp = datetime.now().strftime('%H:%M:%S')
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'chat_message',
                        'message': message,
                        'user': user.username,
                        'timestamp': timestamp
                    }
                )

        except json.JSONDecodeError:
            print("Invalid JSON received")

    async def chat_message(self, event):
        message = event['message']
        user = event['user']
        timestamp = event['timestamp']

        # Send message to WebSocket with user info and timestamp
        await self.send(text_data=json.dumps({
            'message': message,
            'username': user,
            'timestamp': timestamp,
            'typing': False
        }))

    async def user_typing(self, event):
        typing = event['typing']
        sender_username = event['sender']

        await self.send(text_data=json.dumps({
            'typing': typing,
            'username': sender_username
        }))
