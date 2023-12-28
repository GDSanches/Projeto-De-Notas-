from django import get_version
from django.views.generic import TemplateView
from .models import  Nota, Usuario
from myapp.forms import formularioUsuario , CustomLoginForm , formularioNota
from django.shortcuts import render
from .serializers import UsuarioSerializer, NotaSerializer
from rest_framework import generics
from django.contrib.auth.views import LoginView
#from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import HttpResponse


class home(TemplateView):
    template_name = 'home.html'

    def get(self, *args, **kwargs):
        
        return super().get(*args, **kwargs)

def salvar_nota(request):
        form = formularioNota(request.POST)
        if form.is_valid():
          form.save()
          form = formularioNota()

        context = {
            'form': form
        }
        return render(request, 'cria-nota.html', context=context)


class Usuario_List(generics.ListCreateAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class Usuario_Detail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Usuario.objects.all()
  serializer_class = UsuarioSerializer

class Nota_List(generics.ListCreateAPIView):
  queryset = Nota.objects.all()
  serializer_class = NotaSerializer

class Nota_Detail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Nota.objects.all()
  serializer_class = NotaSerializer
  
class CustomLoginView(LoginView):
    template_name = 'login.html'  
    authentication_form = CustomLoginForm  