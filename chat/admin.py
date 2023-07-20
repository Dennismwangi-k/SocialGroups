from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message, User, Jobs, Country_Location

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(User)

admin.site.register(Jobs)

admin.site.register(Country_Location)