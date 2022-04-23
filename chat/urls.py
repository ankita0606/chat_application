from django.urls import path

from .views import *

urlpatterns = [
    path('', RoomEntryView.as_view(), name='room_entry'),
    path('<str:room_name>/', ChatRoomView.as_view(), name='room')
]