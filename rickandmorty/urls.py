"""rickandmorty URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from rickandmorty.views import ver_capitulos, inf_episodio, informacionp,lugar,buscar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',ver_capitulos,name='episodios'),
    path('episodio/<str:id>',inf_episodio,name='inf_episodio'),
    path('personaje/<str:id>',informacionp,name='informacionp'),
    path('lugar/<str:id>',lugar,name='lugar'),
    path('buscar/',buscar,name='buscar')
]
