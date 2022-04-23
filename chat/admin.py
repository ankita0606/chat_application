from django.contrib import admin
from .models import *
# Register your models here.

class UserAdmin(admin.ModelAdmin):
	pass
admin.site.register(User, UserAdmin)

class MessageAdmin(admin.ModelAdmin):
	list_display = ('author', 'content', 'timestamp', 'room')
admin.site.register(Message, MessageAdmin)

class ChatRoomAdmin(admin.ModelAdmin):
	list_display = ('name', 'private',)
admin.site.register(ChatRoom, ChatRoomAdmin)