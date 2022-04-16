from django.urls import path

from .views import RoomEntryView, ChatRoomView , AppRoom

urlpatterns = [
    path('', RoomEntryView.as_view(), name='room_entry'),
    path('whatsapp/', AppRoom.as_view(), name='app_room'),
    path('<str:room_name>/', ChatRoomView.as_view(), name='room')
]