from django.db import models
# Create your models here.

class Estudiante(models.Model):
    identificacion=models.CharField("id",max_length=50)
    nombre=models.CharField('nombre',max_length=100, blank=False,null =False)
    apellido=models.CharField('apellido,',max_length=100, blank=False,null=False)
    telefono=models.CharField('telefono',max_length=50, blank=True,null=True)
    email=models.EmailField('correo',max_length=100,blank=True,null=True)


    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name ='estudiante'
        verbose_name_plural='estudiantes'
    
