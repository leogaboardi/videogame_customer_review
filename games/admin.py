from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Review)
admin.site.register(User)