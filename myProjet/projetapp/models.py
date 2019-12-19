from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class Client(models.Model):
    nom = models.CharField(max_length=155)
    description = models.TextField()
    site_internet = models.URLField(null=True, blank=True)
    image = models.ImageField(upload_to="clent", default="omar-sy-by-rachel.jpg", blank=True)
    adress = models.CharField(max_length=155)
    contact = models.CharField(max_length=155)

    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nom

class Projet(models.Model):
    client = models.ForeignKey(Client, related_name='projet_client', on_delete=models.CASCADE)
    titre = models.CharField(max_length=150)
    description = models.CharField(max_length=150, null=True)
    contenu = models.TextField(null=True)
    cahier_de_charge = models.FileField( upload_to='projet/categorie/',null=True )
    progression = models.PositiveIntegerField(default=0)
    budjet = models.CharField(max_length=50)
    dpense = models.CharField(max_length=100)
    isTermine = models.BooleanField(default=False)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Projet'
        verbose_name_plural = 'Projets'

    def __str__(self):
        return self.titre

class Tache_projet(models.Model):
    projet = models.ForeignKey(Projet, related_name='tache_projet', on_delete=models.CASCADE)
    #user = models.ForeignKey(User, related_name='user_tache', on_delete=models.CASCADE)
    tache = models.CharField(max_length=225)
    progrssion = models.PositiveIntegerField(default=0)
    isTermine = models.BooleanField(default=False)

    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tache


class Commit(models.Model):
    id_commit = models.CharField(max_length=155)
    tache = models.ForeignKey(Tache_projet, related_name='commit_projet', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_commit', on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=150)
    description = models.TextField(null=True)
    lien_git = models.URLField()
    
    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ['date_update']
class Profile(models.Model):
    """Model definition for UserProfile."""

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile_user")
    image = models.ImageField(upload_to="profile", default="omar-sy-by-rachel.jpg")
    fonction = models.CharField(max_length=155)
    promotion = models.CharField(max_length=155)
    adress = models.CharField(max_length=155)
    contact = models.CharField(max_length=155)

    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)


    class Meta:
        """Meta definition for UserProfile."""

        verbose_name = 'UserProfile'
        verbose_name_plural = 'UserProfiles'

    def __str__(self):
        """Unicode representation of UserProfile."""
        return self.user.username


    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    # @receiver(post_save, sender=User)
    # def save_user_profile(sender, instance, created, **kwargs):
    #     instance.profile.save()

class TacheUser(models.Model):
    projet = models.ForeignKey(Projet, related_name='user_projet', on_delete=models.CASCADE)
    tache = models.ForeignKey(Tache_projet, related_name='user_tache', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_tachecommit', on_delete=models.CASCADE)
    durre =  models.TimeField(auto_now_add=True) 

    statut = models.BooleanField(default=True)
    date_add =  models.DateTimeField(auto_now_add=True)
    date_update =  models.DateTimeField(auto_now=True)



#python manage.py admin_generator projetapp >> projetapp/admin.py
