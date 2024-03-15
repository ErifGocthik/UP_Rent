from django.contrib.auth.forms import UserCreationForm
from django.forms import forms


class CustomUserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': 'form-control'})

        for field in list(self.fields.values()):
            field.widget.attrs.update({'class': 'form-control'})