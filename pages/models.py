from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    id =        models.AutoField(primary_key=True)
    title =     models.CharField(max_length=20, verbose_name="Titulo")
    subtitle =  models.CharField(max_length=50, verbose_name="Subtitulo")
    content =   RichTextField(verbose_name="Texto")
    image =     models.ImageField(upload_to='page_imagen', null=True, blank=True, verbose_name="Imagen")
    autor =     models.ForeignKey(User, on_delete=models.CASCADE)
    created =   models.DateTimeField(auto_now_add=True)
    updated =   models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - Autor: {self.autor}'