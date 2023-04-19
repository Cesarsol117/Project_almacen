from django import forms
# registros
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# creacion de formularios
class HerraFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    ubicacion = forms.CharField()

class InsuFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    ubicacion = forms.CharField()
    fecha_vence = forms.DateField()

class RepuFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    maquina = forms.CharField(max_length=50)
    cantidad = forms.IntegerField()
    ubicacion = forms.CharField()

class TecFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    email = forms.EmailField()

#  creacion del formulario
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    # clase anidada que configura el usercreation
    class Meta:
        model = User 
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos de los formularios le asigna un valor vacio.
# para la edicion de usuarios
class UserEditForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="ingrese Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Modificar Nombre")
    last_name = forms.CharField(label="Modificar Apellido")
    # clase anidada que configura el usercreation
    class Meta:
        model = User 
        fields = ["email", "password1", "password2", "first_name", "last_name"]
        help_texts = {k:"" for k in fields} #para cada uno de los campos de los formularios le asigna un valor vacio.
