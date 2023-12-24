from django import forms
#from .models import ItemBatch
from myapp.models import Usuario
from django.contrib.auth.forms import AuthenticationForm



class formularioUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
    
    usuario = forms.CharField( max_length=50, required=True)
    senha = forms.CharField( max_length=50, required=True)


class CustomLoginForm(AuthenticationForm):
    
    usuario = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))