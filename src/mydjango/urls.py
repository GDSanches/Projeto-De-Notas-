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





urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('login/',views.login, name='form_login'),
    path('home/', views.home.as_view(), name='site'),
    path("api/users/", views.Usuario_List.as_view()),
    path("api/users/<int:pk>/", views.Usuario_Detail.as_view()),
    path("api/notes/", views.Nota_List.as_view()),
    path("api/notes/<int:pk>/", views.Nota_Detail.as_view()),

]
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
