from http.client import HTTPResponse

from django.http import HttpResponse
from django.urls import path, reverse_lazy
from django.views.generic import CreateView

from rent_app.forms import PropertyCreateForm
from rent_app.models import Property
from rent_app.views import PropertyListView, PropertyDetailView, RequestFormView, RequestsListView, PropertyCreateView, \
    RequestDetailView, request_accept_view, request_denied_view, RentersListView

app_name = 'rent_app'

urlpatterns = [
    path('main/', PropertyListView.as_view(), name='main'),
    path('property/<int:pk>/', PropertyDetailView.as_view(), name='property_detail'),
    path('request/<int:pk>/', RequestFormView.as_view(), name='request_form'),
    path('moder/requests/', RequestsListView.as_view(), name='requests'),
    path('moder/request-detail/<int:pk>/', RequestDetailView.as_view(), name='request'),
    path('property_create/', PropertyCreateView.as_view(), name='property_create'),
    path('request_accept/<int:pk>/', request_accept_view, name='request_accept'),
    path('request_denied/<int:pk>/', request_denied_view, name='request_denied'),
    path('personal/renters/', RentersListView.as_view(), name='renters')
]