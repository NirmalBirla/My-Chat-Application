from django.urls import path
from .views import register, user_login, index, chat_room, user_logout

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('index/', index, name='index'),
    path('chat/<str:room_name>/', chat_room, name='chat_room'),
    path('logout/', user_logout, name='logout'),
]