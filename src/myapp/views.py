from django import get_version
from django.views.generic import TemplateView
from .models import  Nota, Usuario
from myapp.forms import formularioUsuario , CustomLoginForm
from django.shortcuts import render
from .serializers import UsuarioSerializer, NotaSerializer
from rest_framework import generics
from django.contrib.auth.views import LoginView

# Create your views here.



class home(TemplateView):
    template_name = 'home.html'

    def get(self, *args, **kwargs):
        
        return super().get(*args, **kwargs)
    
class cria_nota(TemplateView):
    template_name = 'cria-nota.html'

    def get(self, *args, **kwargs):
        
        return super().get(*args, **kwargs)


def login(request):

    if request.method == "GET":
        form = formularioUsuario()

        context = {
            'form': form
        }
        return render(request, 'login.html', context= context)
    else:
        form = formularioUsuario(request.POST)
        
        if form.is_valid():
            login =form.save()
            form = formularioUsuario()

        
        context = {
            'form': form
        }
        return render(request, 'login.html', context= context)
    
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