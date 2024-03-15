from django import forms
from django.forms import TextInput, NumberInput, Textarea

from rent_app.models import Request, Property


class RequestCreateForm(forms.ModelForm):
    class Meta:
        model = Request
        exclude = ['id', 'created_at', 'updated_at', 'status', 'user', 'property']


class PropertyCreateForm(forms.ModelForm):
    class Meta:
        model = Property
        exclude = ['renter']
        widgets = {
            'price': NumberInput(attrs={'placeholder': '9999999'}),
            'address': TextInput(attrs={'placeholder': 'Город, улица, номер улицы'}),
            'short_description': TextInput(attrs={'placeholder': 'Краткое описание'}),
            'description': Textarea(attrs={'placeholder': 'Подробное описание'}),
            'phone_number': TextInput(attrs={'placeholder': '7(999)999-99-99 или 99-99-99'}),
            'space': NumberInput(attrs={'placeholder': '99 м²'}),
        }