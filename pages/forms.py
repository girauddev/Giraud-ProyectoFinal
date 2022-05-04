from django import forms
from django.contrib.auth.models import User
from .models import Page

class PageForm(forms.ModelForm):
    class Meta:
        model =     Page
        fields =    ['title', 'subtitle', 'content', 'image', 'autor']
        widgets =   {
                    'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Titulo'}),
                    'subtitle': forms.TextInput(attrs={'class':'form-control','placeholder':'Subtitulo'}),
                    'autor' : forms.TextInput(attrs={'class':'form-control','value':'','id':'autor', 'type':'hidden'})
                    }