from django import forms
from .models import Desocupado

class DesocupadoForm(forms.ModelForm):
    
    class Meta:
        model = Desocupado
        fields = ('title', 'text',)
