from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, verbose_name="Titulo")
    content = models.CharField(max_length=50, verbose_name="Contenido Abreviado")
    texto = RichTextField(verbose_name="Texto del Blog")
    usuario = models.CharField(max_length=50)

    def __str__(self):
        return self.title