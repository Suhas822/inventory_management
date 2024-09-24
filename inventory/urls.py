from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import ItemCreateView, ItemDetailView, RegisterUser

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("items/", ItemCreateView.as_view(), name="item_create"),
    path("items/<int:pk>/", ItemDetailView.as_view(), name="item_detail"),
]
