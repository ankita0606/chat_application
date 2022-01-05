from django.shortcuts import render
from django.views.generic.base import TemplateView


class RoomEntryView(TemplateView):
    '''
    This view enables users to enter a chat room 
    '''
    template_name = "chat/index.html"


class ChatRoomView(TemplateView):
    '''
    This view enables users to chat in a specific room
    '''
    template_name = "chat/room.html"

    def get_context_data(self, **kwargs):
        context = super(ChatRoomView, self).get_context_data(**kwargs)
        context['room_name'] = self.kwargs['room_name']
        return context
