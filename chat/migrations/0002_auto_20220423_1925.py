# Generated by Django 3.1.5 on 2022-04-23 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='room_message', to='chat.chatroom'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='chatroom',
            name='private',
            field=models.BooleanField(default=False),
        ),
    ]
