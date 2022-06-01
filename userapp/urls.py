from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('register/', views.RegistrationAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh-token', TokenRefreshView.as_view(), name='refreshtoken'),
    path('users', views.UserList.as_view(), name = 'list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name = 'user-list')
]
