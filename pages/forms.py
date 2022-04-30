from django import forms
from django.contrib.auth.models import User


class PageForm(forms.Form):
    title = forms.CharField(max_length=20)
    content = forms.CharField(max_length=50)
    texto = forms.CharField(widget=forms.Textarea)
    usuario = forms.CharField(max_length=50)

class SearchPage(forms.Form):
    titulo = forms.CharField(max_length=20)

