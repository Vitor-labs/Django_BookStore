from django.urls import path
from authentication.views import ( RegisterView, VerifyEmailView, LoginAPIView, 
                              RequestPasswordResetEmail, PasswordTokenCheckAPI,
                              SetNewPasswordAPIView
                            )
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('verify-email/', VerifyEmailView.as_view(), name='email-verification'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('request-password-reset/', RequestPasswordResetEmail.as_view(), name='email-password-reset'),
    path('password-reset/<token>/', PasswordTokenCheckAPI.as_view(), name='password-reset'),
    path('password-reset-complete/', SetNewPasswordAPIView.as_view(), name='password-reset-complete'),
    ]