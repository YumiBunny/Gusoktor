from django.db import models
from django.utils import timezone

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fechaDeNacimiento = models.DateField()
    dni = models.CharField(max_length=20)
    experiencialaboral = models.CharField(max_length=70)
    profesion = models.ForeignKey('Rubro')
    formacion = models.CharField(max_length=70)
    habilidades = models.CharField(max_length=70)
    desocupado = models.BooleanField()

    def __str__(self):
            return self.title

class Rubro(models.Model):
    tipoDeTrabajo = models.CharField(max_length=30)

    def __str__(self):
            return self.title

class Empleo(models.Model):
    persona = models.ForeignKey('Persona')
    empresa = models.ForeignKey('Empresa')
    oferta = models.ForeignKey('Oferta')
    inicioContrato = models.DateField()
    finContrato = models.DateField()

    def __str__(self):
            return self.title

class Oferta(models.Model):
    empresa = models.ForeignKey('Empresa')
    activa = models.BooleanField()
    necesidad = models.ForeignKey('Rubro')
    inicioContrato = models.DateField()
    finContrato = models.DateField()

    def __str__(self):
            return self.title

class Agencia(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
            return self.title

class Empresa(models.Model):
    cuit = models.CharField(max_length=30)
    rubro = models.ForeignKey('Rubro')
    razonSocial = models.CharField(max_length=50)
    activa = models.BooleanField()

    def __str__(self):
            return self.title

# Create your models here.
