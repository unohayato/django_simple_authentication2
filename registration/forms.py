from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.conf import settings

from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

User = get_user_model()

class SignUpForm(UserCreationForm):
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")
    
  def save(self, commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_data["email"]
    user.save()
    return user