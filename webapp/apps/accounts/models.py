from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    photo = models.ImageField('Foto', upload_to='photos')
    cell_phone = models.CharField('Celular', max_length=16)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    class Meta:
        verbose_name = 'Perfil do usuario'
        verbose_name_plural = 'Perfis dos usuarios'

    def __str__(self):
        return self.user.username