from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

from auth.forms import CustomUserCreateForm
from auth.views import user_logout

app_name = 'custom_auth'

urlpatterns = [
    path('sign-in/', LoginView.as_view(template_name='sign_in.html', next_page=reverse_lazy('rent_app:main')), name='sign_in'),
    path('sign-up/', CreateView.as_view(template_name='sign_up.html',
                                        success_url=reverse_lazy('auth:sign_in'),
                                        form_class=CustomUserCreateForm,
                                        model=User), name='sign_up'),
    path('logout/', user_logout, name='logout'),
]