from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe

from . import models


class ClientAdmin(admin.ModelAdmin):

    list_display = ('id','view_image','nom','site_internet','adress','contact', 'image','statut','date_add','date_update',)
    list_filter = ('statut','date_add','date_update',)
    search_fields = ('nom','site_internet',)
    actions = ('active', 'desactive')
    date_hierarchy = "date_add"
    list_display_links = ('id','nom',)
    list_per_page = 30
    oerdering = ['nom']
    
    fieldsets = [
        ('Addresse et statut',{
            'fields':['adress','statut']
        }),
        ('Contacts',{
            'fields':['site_internet','contact',]
        }),
        ('Image',{
            'fields':['image']
        }),
        
    ]
    
    def active(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été activée")
    active.short_description = 'active'
    
    def desactive(self, request, queryset):
        queryset.update(statut= False)
        self.message_user(request, "La selection a bien été desactivée")
    desactive.short_description = 'desactive'

    def view_image(self,obj):
        return mark_safe('<img src="{img_url}" width="50px", heigth="50px"/>'.format(img_url=obj.image.url))

class ProjetAdmin(admin.ModelAdmin):

    list_display = ('id','client','titre','description','cahier_de_charge','progression','isTermine','date_debut','date_fin','statut','date_add','date_update',)
    list_filter = ('client','statut','date_add', 'date_update')
    search_fields = ('titre','progression',)
    actions = ('active', 'desactive')
    date_hierarchy = "date_add"
    list_display_links = ('id','titre')
    list_per_page = 30
    oerdering = ['nom']
    
    fieldsets = [
        ('Client',{
            'fields':['client']
        }),
        ('Informations projet',{
            'fields':['titre','description','cahier_de_charge']
        }),
        ('Etat',{
            'fields':['progression','isTermine',]
        }),
        
    ]
        
    def active(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été activée")
    active.short_description = 'active'
        
    def desactive(self, request, queryset):
        queryset.update(statut= False)
        self.message_user(request, "La selection a bien été desactivée")
    desactive.short_description = 'desactive'

class Tache_projetAdmin(admin.ModelAdmin):

    list_display = ('id','projet','tache','progrssion','isTermine','statut','date_add','date_update',)
    list_filter = ('projet','statut','date_add','date_update',)
    search_fields = ('tache',)
    actions = ('active', 'desactive')
    date_hierarchy = "date_add"
    list_display_links = ('id','tache',) 
    list_per_page = 30
    oerdering = ['tache',]
    
    fieldsets = [
        ('Projet',{
            'fields':['projet']
        }),
        ('Informations tache',{
            'fields':['tache',]
        }),
        ('Etat',{
            'fields':['progrssion','isTermine','statut']
        }),
        
    ]
        
    def active(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été activée")
    active.short_description = 'active'
        
    def desactive(self, request, queryset):
        queryset.update(statut= False)
        self.message_user(request, "La selection a bien été desactivée")
    desactive.short_description = 'desactive'


class CommitAdmin(admin.ModelAdmin):

    list_display = ('id','id_commit','tache','user','commentaire','description','lien_git','statut','date_add','date_update',)
    list_filter = ('tache','user','statut','date_add','date_update',)
    
    search_fields = ('user','lien_git',)
    actions = ('active', 'desactive')
    date_hierarchy = "date_add"
    list_display_links = ('id','commentaire',)
    list_per_page = 30
    oerdering = ['id_commit',]
            
    def active(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été activée")
    active.short_description = 'active'
            
    def desactive(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été desactivée")
    desactive.short_description = 'desactive'
    
    fieldsets = [
        ('Travail',{
            'fields':['tache']
        }),
        ('User',{
            'fields':['user','lien_git',]   
        }),
        ('Informations commit',{
            'fields':['id_commit','commentaire','description']
        }),
        
            
    ]



class ProfileAdmin(admin.ModelAdmin):

    list_display = ('id','view_image','user','image','fonction','promotion','adress','contact','statut','date_add','date_update',)
    list_filter = ('user','statut','date_add','date_update',)
    
    search_fields = ('user','contact',)
    actions = ('active', 'desactive')
    date_hierarchy = "date_add"
    list_display_links = ('id','view_image',)
    list_per_page = 30
    oerdering = ['fonction',]
            
    def active(self, request, queryset):
        queryset.update(statut = True)
        self.message_user(request, "La selection a bien été activée")
    active.short_description = 'active'

    def desactive(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été desactivée")
    desactive.short_description = 'desactive'


    def view_image(self,obj):
        return mark_safe('<img src="{img_url}" width="50px", heigth="50px"/>'.format(img_url=obj.image.url))

class TacheUserAdmin(admin.ModelAdmin):

    list_display = ('id','projet','tache','user','durre','statut','date_add','date_update',)
    list_filter = ('projet','tache','user','statut','date_add','date_update',)
    
    search_fields = ('projet','user','durre')
    actions = ('active', 'desactive')
    date_hierarchy = "date_add"
    list_display_links = ('id','tache',)
    list_per_page = 30
    oerdering = ['durre',]  
                
    def active(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été activée")
    active.short_description = 'active'
                
    def desactive(self, request, queryset):
        queryset.update(statut= True)
        self.message_user(request, "La selection a bien été desactivée")
    desactive.short_description = 'desactive'


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Client, ClientAdmin)
_register(models.Projet, ProjetAdmin)
_register(models.Tache_projet, Tache_projetAdmin)
_register(models.Commit, CommitAdmin)
_register(models.Profile, ProfileAdmin)
_register(models.TacheUser, TacheUserAdmin)
