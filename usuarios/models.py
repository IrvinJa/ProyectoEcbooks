
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save

class CatalogoSexo(models.Model):
    nombre=models.CharField(max_length=50)
    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='catalogo_sexo_creacion', blank=True, null=True,)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='catalogo_sexo_modificacion', blank=True, null=True,)
    fecha_modificacion = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True,)

    def __str__(self):
        catalogo_sexo="{}".format(self.nombre)
        return catalogo_sexo

    class Meta:
        verbose_name = 'Catalogo sexo'
        verbose_name_plural = 'Catalogo sexos'
        db_table = 'catalogo_sexo'
        ordering = ['pk']

class Usuario(models.Model):
    usuario= models.ForeignKey(User, on_delete=models.CASCADE, related_name='usuario_usuario', blank=True, null=True)
    nombres = models.CharField(max_length=50)
    apellido_paterno=models.CharField(max_length=80)
    apellido_materno=models.CharField(max_length=80)
    edad=models.IntegerField(null=True)
    email = models.EmailField(max_length=255, unique=True, null=True)
    sexo= models.ForeignKey(CatalogoSexo, on_delete=models.CASCADE, related_name='usuario_catalogosexo', blank=True, null=True)

    usuario_creacion = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='usuario_creacion_usuario', blank=True, null=True,)
    fecha_creacion = models.DateTimeField(auto_now_add=True, editable=False, blank=True, null=True)
    usuario_modificacion = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, related_name='usuario_modificacion_usuario', blank=True, null=True,)
    fecha_modificacion = models.DateTimeField(auto_now=True, editable=False, blank=True, null=True,)
    
    def __str__(self):
        usuario="{} {} {}".format(self.nombres, self.apellido_paterno, self.apellido_materno)
        return usuario
    
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'usuario'
        ordering = ['pk']




