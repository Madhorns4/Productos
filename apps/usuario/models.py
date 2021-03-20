from django.db import models

# Create your models here.

class Usuario(models.Model):
    user_id = models.AutoField(primary_key=True)
    user = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    estado = models.IntegerField(blank=False, default=1)
    
    class Meta:
        verbose_name= 'Usuario',
        verbose_name_plural= 'Usuarios',
        db_table= 'usuario'