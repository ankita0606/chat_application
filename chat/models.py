from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.
class User(AbstractUser):
	"""
	Description: Extends the django user model
	"""
	profile_picture = models.ImageField(default='default.png', upload_to='profile_pics')

	class Meta:
		ordering = ('username',)

	def __str__(self):
		return self.username

	def get_full_name(self):
		if self.first_name:
			return str(self.first_name) + ' ' + str(self.last_name)
		else:
			return str(self.username)


class ChatRoom(models.Model):
	"""
	Description: Contains an individual instance of a chat room
	"""
	name = models.CharField(max_length=150, unique=True)
	private = models.BooleanField(default=False)
	allowed_member_list = models.ManyToManyField(User, blank=True)

	class Meta:
		pass

	def __str__(self):
		return self.name


class Message(models.Model):
	"""
	Description: Contains an individual message instance
	"""
	author = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
	content = models.TextField()
	timestamp = models.DateTimeField(auto_now_add=True)
	room = models.ForeignKey(ChatRoom, related_name='room_message', on_delete=models.CASCADE)

	class Meta:
		None

	def __str__(self):
		return self.author.username


