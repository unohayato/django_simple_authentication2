from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import SignUpform

class SognUpView(CreateView):
  form_class = SignUpform
  success_url = reverse_lazy('login')
  template_name = 'registration/signup.html'
  