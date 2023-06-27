from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.UserCreate.as_view(), name='account-create'),
]
