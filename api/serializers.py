from rest_framework.serializers import ModelSerializer, ValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer
from .models import User

class RegistrationSerializer(ModelSerializer, RegisterSerializer):
    class Meta:
        model = User
        fields = ["email", "password1", "password2",]

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user was found with this email.")
        return email
    
class CUserDetailsSerializer(UserDetailsSerializer, ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'last_login', 'date_joined', 'is_active', "is_superuser", "is_staff"]
        read_only_fields = ['email', 'last_login', 'date_joined', 'is_active',]