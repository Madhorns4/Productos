from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('user','password','name','last_name')
        label = {
            'user' : 'Nombre de usuario',
            'password' : 'Contraseña',
            'name' : 'Nombre',
            'last_name' : 'Apellido'
        }
        widgets = {
            'user': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'password': forms.TextInput(
                attrs = {
                    'type': 'password',
                    'class': 'form-control',
                }
            ),
            'name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
            'last_name': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                }
            ),
        }