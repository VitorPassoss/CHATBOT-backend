from django.urls import path
from . import views
from authentication.services.auth_token import CustomTokenObtainPairView

urlpatterns = [
    path("login/", CustomTokenObtainPairView.as_view(),name="login-v1"),
    path('user/', views.DetailsUser.as_view(), name='user')
]
