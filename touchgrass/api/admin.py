from django.contrib import admin

from .models import Post, AdminMessage, Profile

admin.site.register(Post)
admin.site.register(AdminMessage)
admin.site.register(Profile)
