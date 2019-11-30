from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'view_image',
        'nom',
        'site_internet',
        'adress',
        'contact',
        'image',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_update',
        'id',
        'nom',
        'description',
        'site_internet',
        'adress',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )

    def view_image(self,obj):
        return mark_safe('<img src="{img_url}" width="50px", heigth="50px"/>'.format(img_url=obj.image.url))

class ProjetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'client',
        'titre',
        'description',
        'cahier_de_charge',
        'progression',
        'isTermine',
        'date_debut',
        'date_fin',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'client',
        'isTermine',
        'date_debut',
        'date_fin',
        'statut',
        'date_add',
        'date_update',
        'id',
        'client',
        'titre',
        'description',
        'cahier_de_charge',
        'progression',
        'isTermine',
        'date_debut',
        'date_fin',
        'statut',
        'date_add',
        'date_update',
    )


class Tache_projetAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'projet',
        'tache',
        'progrssion',
        'isTermine',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'projet',
        'isTermine',
        'statut',
        'date_add',
        'date_update',
        'id',
        'projet',
        'tache',
        'progrssion',
        'isTermine',
        'statut',
        'date_add',
        'date_update',
    )


class CommitAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'id_commit',
        'tache',
        'user',
        'commentaire',
        'description',
        'lien_git',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'tache',
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'id_commit',
        'tache',
        'user',
        'commentaire',
        'description',
        'lien_git',
        'statut',
        'date_add',
        'date_update',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'view_image',
        'user',
        'image',
        'fonction',
        'promotion',
        'adress',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'user',
        'image',
        'fonction',
        'promotion',
        'adress',
        'contact',
        'statut',
        'date_add',
        'date_update',
    )

    def view_image(self,obj):
        return mark_safe('<img src="{img_url}" width="50px", heigth="50px"/>'.format(img_url=obj.image.url))

class TacheUserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'projet',
        'tache',
        'user',
        'durre',
        'statut',
        'date_add',
        'date_update',
    )
    list_filter = (
        'projet',
        'tache',
        'user',
        'statut',
        'date_add',
        'date_update',
        'id',
        'projet',
        'tache',
        'user',
        'durre',
        'statut',
        'date_add',
        'date_update',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Client, ClientAdmin)
_register(models.Projet, ProjetAdmin)
_register(models.Tache_projet, Tache_projetAdmin)
_register(models.Commit, CommitAdmin)
_register(models.Profile, ProfileAdmin)
_register(models.TacheUser, TacheUserAdmin)
