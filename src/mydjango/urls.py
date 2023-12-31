"""mydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from myapp import views 
from myapp.views import CustomLoginView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    path('', CustomLoginView.as_view(), name='login'),
    path('home/', views.home.as_view(), name='site'),
    path("api/usuario/", views.Usuario_List.as_view()),
    #path("api/usuario/<int:pk>/", views.Usuario_Detail.as_view()),
    path("api/notas/", views.Nota_List.as_view()),
    path("api/notas/<int:pk>/", views.Nota_Detail.as_view()),
    path ('salvar-nota/',views.salvar_nota, name='salvar-nota'),

]
