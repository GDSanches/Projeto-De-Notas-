from django import get_version
from django.views.generic import TemplateView
from .models import  Nota
from myapp.forms import formularioUsuario
from django.shortcuts import render
# Create your views here.



class home(TemplateView):
    template_name = 'home.html'

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
    
def notas_list(request):
    notas = Nota.objects.all()
    return render(request, 'home.html', {'notas': notas})