from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

class User(AbstractUser, PermissionsMixin):
    other_field = models.CharField(null=True, max_length=255)  # would remove later

    def __str__(self) -> str:
        return f"<user {self.username}>"
    
    class Meta:
        db_table = "user"