from django import forms
#from .models import ItemBatch
from myapp.models import Usuario




class formularioUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = "__all__"
    
    usuario= forms.CharField( max_length=50, required=True)
    senha= forms.CharField( max_length=50, required=True)