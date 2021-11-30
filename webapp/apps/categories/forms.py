from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        exclude = ('user', 'created_on' , 'updated_on',)