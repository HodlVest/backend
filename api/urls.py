from django.urls import path
from . import views

urlpatterns = [
    # Auth patterns
    path('auth/registration/account-email-verification-sent/', views.NotFoundView().as_view(), name="not-found"),
    path('auth/registration/account-confirm-email/<str:key>/', views.VerifyEmail().as_view(), name="verify_email"),
    path('auth/password/reset/confirm/<int:uid64>/<str:token>/', views.PasswordReset().as_view(), name="password_reset_confirm"),
    path('auth/google/', views.GoogleLogin.as_view(), name="google_login"),
    
    # Others
]
