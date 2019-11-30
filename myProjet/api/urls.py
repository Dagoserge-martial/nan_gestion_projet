"""le_resto URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .import views

from rest_framework.routers import DefaultRouter

from .apiviews import ClientViewSet, ProjetViewSet, Tache_projetViewSet, CommitViewSet, TacheUserViewSet, ProfileViewSet

router = DefaultRouter()
router.register('client', ClientViewSet, base_name='client')
router.register('Projet', ProjetViewSet, base_name='Projet')
router.register('Tache_projet', Tache_projetViewSet, base_name='Tache_projet')
router.register('Commit', CommitViewSet, base_name='Commit')
router.register('TacheUser', TacheUserViewSet, base_name='TacheUser')
router.register('Profile', ProfileViewSet, base_name='Profile')

urlpatterns = [
   
]

urlpatterns += router.urls
