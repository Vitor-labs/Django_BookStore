from django.urls import path
from inventory.views import RegisterView, VerifyEmailView, LoginAPIView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='email-verification'),
    path('login/', LoginAPIView.as_view(), name='login'),
    ]