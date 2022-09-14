from django.db import models

# Create your models here.

class Curso(models.Model):

    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()



#python manage.py sqlmigrate AppCoder 0001   