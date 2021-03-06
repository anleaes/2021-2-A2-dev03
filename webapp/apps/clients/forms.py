from django import forms
from .models import Client

class ClientForm(forms.ModelForm):

    class Meta:
        model = Client
        exclude = ('user', 'created_on' , 'updated_on',)