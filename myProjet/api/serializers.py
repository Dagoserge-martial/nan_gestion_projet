from rest_framework import serializers
from projetapp.models import *
from .models import *
from drf_dynamic_fields import DynamicFieldsMixin

class TacheUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacheUser
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class CommitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commit
        fields = '__all__'

class Tache_projetSerializer(serializers.ModelSerializer):
    commit_projet = CommitSerializer(many=True, required=False)
    user_tache = TacheUserSerializer(many=True, required=False)
    class Meta:
        model = Tache_projet
        fields = '__all__'

class ProjetSerializer(serializers.ModelSerializer):
    tache_projet = Tache_projetSerializer(many=True, required=False)
    user_projet = TacheUserSerializer(many=True, required=False)
    class Meta:
        model = Projet
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    projet_client = ProjetSerializer(many=True, required=False)
    class Meta:
        model = Client
        fields = '__all__'
