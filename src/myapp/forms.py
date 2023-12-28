from django import forms
#from .models import ItemBatch
from myapp.models import Usuario,Nota
from django.contrib.auth.forms import AuthenticationForm



class formularioNota(forms.ModelForm):

    class Meta:
        model = Nota
        fields = "__all__"
    
    Titulo = forms.CharField( max_length=50, required=True)
    conteudo = forms.CharField( required=True)

class formularioUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
    
    usuario = forms.CharField( max_length=50, required=True)
    senha = forms.CharField( max_length=50, required=True)


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Usuário",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Digite seu nome de usuário",
                "class": "form-control"
            }
        )
    )
    # Sobrescrevendo o campo de senha
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Digite sua senha",
                "class": "form-control"
            }
        )
    )