from rest_framework import viewsets
from rest_framework import generics
from rest_framework import filters
from projetapp.models import *
from .models import *

from .serializers import ClientSerializer, ProjetSerializer, Tache_projetSerializer, CommitSerializer, ProfileSerializer, TacheUserSerializer

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ProjetViewSet(viewsets.ModelViewSet):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer

class Tache_projetViewSet(viewsets.ModelViewSet):
    queryset = Tache_projet.objects.all()
    serializer_class = Tache_projetSerializer

class CommitViewSet(viewsets.ModelViewSet):
    queryset = Commit.objects.all()
    serializer_class = CommitSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class TacheUserViewSet(viewsets.ModelViewSet):
    queryset = TacheUser.objects.all()
    serializer_class = TacheUserSerializer
