from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Message

class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ['authorone','authortwo','created','text']

admin.site.register(Message, MessageAdmin)
