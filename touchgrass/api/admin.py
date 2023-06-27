from django.contrib import admin

from .models import Post, AdminMessage

admin.site.register(Post)
admin.site.register(AdminMessage)
