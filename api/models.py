from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    username = None
    
    email = models.EmailField(unique=True, null=False)

    other_field = models.CharField(null=True, max_length=255)  # would remove later

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return f"{self.email}"
    
    class Meta:
        db_table = "user"