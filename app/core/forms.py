from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroDesocupado(UserCreationForm):
    DNI = forms.CharField(max_length=10)
    fecha_de_nacimiento = forms.CharField()
    profesion = forms.CharField()
    experiencia_laboral = forms.CharField()
    formacion = forms.CharField()
    habilidades = forms.CharField()

    class Meta:
        model = User
        # Le pega a user, porq queremos que guarde el usuario,
        # la creación del perfil la manejamos en el metodo de más abajo
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        # Llamamos al save ya definido en el formulario, esto automaticamente
        # crea la empresa y el desocupado que actuan de perfil
        user = super(RegistroDesocupado, self).save()
        # Ahora le digo que rellene al usuario con todos los datos que correspondan
        user.refresh_from_db()
        # Y finalmente cargamos todos los elementos del desocupado desde el formulario
        user.desocupado.DNI = self.cleaned_data.get('DNI')
        user.desocupado.nombre = self.cleaned_data.get('first_name')
        user.desocupado.apellido = self.cleaned_data.get('last_name')
        user.desocupado.fecha_de_nacimiento = self.cleaned_data.get('fecha_de_nacimiento')
        user.desocupado.profesion = self.cleaned_data.get('profesion')
        user.desocupado.experiencia_laboral = self.cleaned_data.get('experiencia_laboral')
        user.desocupado.formacion = self.cleaned_data.get('formacion')
        user.desocupado.habilidades = self.cleaned_data.get('habilidades')
        # Finalmente, guardamos el usuario con el desocupado ya completo
        user.save()
        # Y lo devolvemos
        return user

class RegistroEmpresa(UserCreationForm):
    CUIT = forms.CharField(max_length=10)
    razon_social = forms.CharField()
    rubro = forms.CharField()

    class Meta:
        model = User
        # Le pega a user, porq queremos que guarde el usuario,
        # la creación del perfil la manejamos en el metodo de más abajo
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def save(self):
        # Llamamos al save ya definido en el formulario, esto automaticamente
        # crea la empresa y el desocupado que actuan de perfil
        user = super(RegistroEmpresa, self).save()
        # Ahora le digo que rellene al usuario con todos los datos que correspondan
        user.refresh_from_db()
        # Y finalmente cargamos todos los elementos de la empresa
        user.empresa.CUIT = self.cleaned_data.get('CUIT')
        user.empresa.razon_social = self.cleaned_data.get('razon_social')
        user.empresa.rubro = self.cleaned_data.get('rubro')
        # Finalmente, guardamos el usuario con la empresa ya completo
        user.save()
        # Y lo devolvemos
        return user

##########################################

class RegistroOferta(UserCreationForm):
    posicion_o_cargo = forms.CharField(max_length=40)
    descripcion_del_trabajo = forms.CharField(max_length=50)
    profesion = forms.CharField(max_length=30)
    carga_horaria = forms.CharField(max_length=30)

    def save(self):
        user = super(RegistroOferta, self).save()
        user.refresh_from_db()
        user.empresa.posicion_o_cargo = self.cleaned_data.get('posicion_o_cargo')
        user.empresa.descripcion_del_trabajo = self.cleaned_data.get('descripcion_del_trabajo')
        user.empresa.profesion = self.cleaned_data.get('profesion')
        user.empresa.pcarga_horaria = self.cleaned_data.get('carga_horaria')
        user.save()
        return user

