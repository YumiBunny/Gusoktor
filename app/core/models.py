from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import app.core.patch

# La solución planteada tiene ventajas y desventajas. Como ventaja, se usa el
# sistema de autenticación de django, y no hay que hacer muchas cosas pues ya
# vienen hechas. Cada entidad que es logueable, actua a modo de "perfil" de
# usuario, conteniendo información adicional a los datos básicos que sirven para
# loguear al usuario, etc.
# Además, cada vez que se crea un usuario, sea desde el registro o desde el admin,
# se le crean perfiles asociados (Acá viene la desventaja, si creo un usuario,
# se le crean dos perfiles, uno de desocupado y uno de empresa, a lo cual, siempre
# tengo un perfil que no uso, porq un desocupado no es una empresa, asi que me
# quedan elementos vacíos por varios lados, pero bue)
# Por otro lado, a un usuario se le puede preguntar si es o no un desocupado, o
# si es o no una empresa, y pedir el "perfil" que devuelve o bien una empresa o
# bien un desocupado, dependiendo de lo que se haya cargado.
class Desocupado(models.Model):
    # Las cosas logueables tienen que tener este campo adicional.
    # Estas entidad actuan entonces como perfil de un usuario, y guardan
    # datos adicionales a los que se guarda en un usuario tradicional de Django
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # El resto de los campos son los que yo quiero tener el perfil. Notece que
    # algunos campos como el nombre, el apellido, o el email, ya están incluidos
    # en el usuario de django, pero se pueden clonar tranquilamente acá.
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    # Usen guiones bajos o de lo contrario va a fallar Django
    fecha_de_nacimiento = models.DateField(null=True)
    dni = models.CharField(max_length=20, null=True)
    experiencia_laboral = models.CharField(max_length=70, null=True)
    # Este lo comento porq requiere algunos detalles extras en el form que
    # les queda a ustedes para hacer
    # profesion = models.ForeignKey('Rubro')
    formacion = models.CharField(max_length=70, null=True)
    habilidades = models.CharField(max_length=70, null=True)
    desocupado = models.BooleanField(default=True)

    # Como se representa como texto, o sea, como se ve en el admin
    def __str__(self):
        return "Desocupado: " + str(self.nombre) + " " + str(self.apellido)  + " de " + str(self.user.username)
    

# Si se crea un usuario, se crea automáticamente un Desocupado 
@receiver(post_save, sender=User)
def update_user_desocupado(sender, instance, created, **kwargs):
    if created:
        Desocupado.objects.create(user=instance)
    instance.desocupado.save()

class Empresa(models.Model):
    # La empresa también es logueable, idem desocupado
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # El resto de los campos
    cuit = models.CharField(max_length=30)
    # Idem acá, las relaciones se las dejo a ustedes
    # rubro = models.ForeignKey('Rubro')
    razon_social = models.CharField(max_length=50)

    # Como se representa como texto, o sea, como se ve en el admin
    def __str__(self):
        return "Empresa" + str(self.razon_social) + " de " + str(self.user.username)

    def contratar_desempleado():
       pass

# Si se crea un usuario, se crea automáticamente una Empresa
@receiver(post_save, sender=User)
def update_user_empresa(sender, instance, created, **kwargs):
    if created:
        Empresa.objects.create(user=instance)
    instance.empresa.save()

# El resto de las entidades queda a completar.
# Como hice varios cambios comento las relaciones para que no se rompa nada.

class Rubro(models.Model):
    tipoDeTrabajo = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Empleo(models.Model):
    #persona = models.ForeignKey('Persona')
    #empresa = models.ForeignKey('Empresa')
    #oferta = models.ForeignKey('Oferta')
    inicio_contrato = models.DateField()
    fin_contrato = models.DateField()

    def __str__(self):
        return self.title

class Oferta(models.Model):
    #empresa = models.ForeignKey('Empresa')
    activa = models.BooleanField()
    #necesidad = models.ForeignKey('Rubro')
    inicio_contrato = models.DateField()
    fin_contrato = models.DateField()

    def __str__(self):
        return self.title