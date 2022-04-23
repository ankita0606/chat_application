from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *


class RoomEntryView(LoginRequiredMixin, TemplateView):
    '''
    This view enables users to enter a chat room 
    '''
    template_name = "chat/entry.html"


class ChatRoomView(LoginRequiredMixin,TemplateView ):
    '''
    This view enables users to chat in a specific room
    '''
    template_name = "chat/room.html"

    def get(self, *args, **kwargs):
        # check if room exist in db
        chat_room_obj = ChatRoom.objects.filter(name=self.kwargs['room_name'])
        if not chat_room_obj:
            # create room in db if it doesn't exist
            chat_room_obj = ChatRoom.objects.create(name=self.kwargs['room_name'])
        else:
            # get room object from list of room objects
            chat_room_obj = chat_room_obj[0]
        # check if room is private
        if chat_room_obj.private:
            # redirect if user not part of approved list
            if not self.request.user in chat_room_obj.allowed_member_list.all():
                return redirect('unauthorized_room')
        return super().get(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ChatRoomView, self).get_context_data(**kwargs)
        context['message_list'] = Message.objects.filter(room__name=self.kwargs['room_name'])
        chat_room_obj = ChatRoom.objects.get(name=self.kwargs['room_name'])
        context['room_id'] = chat_room_obj.id
        context['room_name'] = chat_room_obj.name
        return context


