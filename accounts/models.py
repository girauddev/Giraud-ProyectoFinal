from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True)

    def __str__(self):
        return self.user.username

class Mensaje(models.Model):
    id = models.AutoField(primary_key=True)
    mensaje = RichTextField(verbose_name="Mensaje")
    autor = models.CharField(max_length=10, verbose_name="Emitente")
    dest = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Destinatario")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.autor} - Destinatario: {self.dest}'

