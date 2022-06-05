from django.contrib import admin

# Register your models here.

from .models import Message,friend_request


admin.site.register(Message)
admin.site.register(friend_request)

