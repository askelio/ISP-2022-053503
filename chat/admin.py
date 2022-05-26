from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(customer)
admin.site.register(messages_channel)
admin.site.register(messages)

