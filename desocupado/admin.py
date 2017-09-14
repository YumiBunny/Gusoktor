from django.contrib import admin
from .models import Persona
from .models import Rubro
from .models import Empleo
from .models import Oferta
from .models import Agencia
from .models import Empresa

admin.site.register(Persona)
admin.site.register(Rubro)
admin.site.register(Empleo)
admin.site.register(Oferta)
admin.site.register(Agencia)
admin.site.register(Empresa)

# Register your models here.
