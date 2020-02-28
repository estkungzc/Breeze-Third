from django.shortcuts import render
from django.contrib.auth import views as auth_views

# Create your views here.

class MyLoginView(auth_views.LoginView):
    template_name = 'users/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title': 'Login',
        })
        return context