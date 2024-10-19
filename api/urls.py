from django.urls import path
from . import views

urlpatterns = [
    # Auth patterns
    path('auth/registration/account-email-verification-sent/', views.NotFoundView().as_view(), name="not-found"),

    # Others
]
