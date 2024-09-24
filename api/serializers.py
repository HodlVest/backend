from rest_framework.serializers import ModelSerializer, ValidationError
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User

class RegistrationSerializer(ModelSerializer, RegisterSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password1", "password2"]  # might be modified later (TBD)

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user was found with this email.")
        return email
    
    def save(self, request):
        user = super().save(request)
        user.first_name = self.validated_data.get("first_name", None)
        user.last_name = self.validated_data.get("last_name", None)
        user.save()
        return user