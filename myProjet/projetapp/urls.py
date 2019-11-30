"""myProjet URL Configuration

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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .import views

app_name = 'projetapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.list_user, name='list_user'),
    path('<id>/detailuser/', views.detailuser, name='detailuser'),
    #path(r'(?P<id>\d+)/detailuser/$', views.detailuser, name='detailuser'),
    path('projets/', views.projet, name='projet'),
    path('<id>/projetdetail/', views.projetdetail, name='projetdetail'),
    path('commit/', views.commit, name='commit'),
    path('commits/', views.commits, name='commits'),
    path('new_project/', views.newproject, name='newproject'),
    path('user_task/', views.newusetask, name='newusetask'),
    path('login/', views.connexion, name='connexion'),
]
