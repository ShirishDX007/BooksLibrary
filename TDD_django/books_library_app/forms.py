from django import forms
from .models import Catalogue

class AddBookForm(forms.ModelForm):
    class Meta:
        model = Catalogue
        fields = "__all__"

        widgets = {
            'title': forms.fields.TextInput(attrs={'class': 'form-control'}),
            'ISBN': forms.fields.TextInput(attrs={'class': 'form-control'}),
            'author': forms.fields.TextInput(attrs={'class': 'form-control'}),
            'price': forms.fields.TextInput(attrs={'class': 'form-control'}),
            'availability': forms.fields.TextInput(attrs={'class': 'form-control'}),
        }