from django.urls import path, re_path
from . import views
from . views import MyTokenObtainPairView

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', views.getRoutes),
    path('posts/', views.getPosts),

    path('profile/get', views.getProfile),
    path('profile/add', views.addProfile),

    path('admin/messages/send', views.sendAdminMessage),
    path('admin/messages/', views.getAdminMessages),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]