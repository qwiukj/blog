from django.contrib.auth.forms import UserCreationForm
from .models import NewUser

class RegisterForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = NewUser
        fields = ("username", "email")
