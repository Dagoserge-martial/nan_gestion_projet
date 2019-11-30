from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
from . import models

# Create your views here.

def home(request):
    projet_all = models.Projet.objects.all()
    projett = models.Projet.objects.filter(statut=False)
    projetb = models.Projet.objects.filter(isTermine=True)
    projetc = models.Projet.objects.filter(isTermine=False)
    nbpall =projet_all.count()
    nbprojetb = projetb.count()
    nbpt =projett.count()
    nbpc =projetc.count()

    profile = models.User.objects.all()
    print(nbpall)
    data = {
        'projett':projett,
        'nbprojetb':nbprojetb,
        'projet_all':projet_all,
        'projetc': projetc,
        'nbpall':nbpall,
        'nbpt': nbpt,
        'nbpc':nbpc,
        'profile':profile,
    }
    return render(request, 'page/dashboard/dashboard.html', data)

def projet(request):
    return render(request, 'page/dashboard/list_projet.html')

def list_user(request):
    profile_all = models.TacheUser.objects.all()
    users = models.User.objects.all()
    # proj = models.TacheUser.objects.filter(statut=True).filter( projet = models.User.user_tachecommit )
    # print(proj)

    data = {
        'profile_all': profile_all,
        'users': users,
        #'proj':proj,
    }
    return render(request, 'page/dashboard/users.html', data)

def detailuser(request, id):
    profil = models.User.objects.get(pk=id)
    #profil = models.User.objects.get(id=4)
    #nb = profil.user_tachecommit.all().filter(tache = models.Tache_projet.tache )
    nbpt = profil.user_tachecommit.all().count()
    print(nbpt)
    # print(nb)
    data = {
        'profil':profil,
        'nbpt':nbpt,
    }
    #{% url 'detailuser' home.pk %}
    return render(request, 'page/dashboard/detail_user.html', data)

def projetdetail(request):
    return render(request, 'page/dashboard/projetdetail.html')

def commit(request):
    return render(request, 'page/dashboard/commit.html')

def commits(request):
    return render(request, 'page/dashboard/commits.html')

def newproject(request):
    clt = models.Client.objects.filter(statut=True)

    # titre=request.POST.get('titre')
    # description=request.POST.get('description')
    # client=request.POST.get('client')
    # budjet=request.POST.get('budjet')
    # dpense=request.POST.get('dpense')
    # ddebut=request.POST.get('ddebut')
    # dfin=request.POST.get('dfin')
    # file=request.FILES.get('file')

    # print(titre)
    # print(description)
    # print(client)
    # print(budjet)
    # print(dpense)
    # print(ddebut)
    # print(dfin)
    # print(file)

    # try:
    #     projet = models.Projet(titre=titre, description=description, client=client, budjet=budjet, cahier_de_charge=file, dpense=dpense, ddebut=ddebut, dfin=dfin)
    #     projet.save()
    #     print('ok000000000000000')

    # except Exception as err:
    #     print(err,'++++++++++++++++++++++')
        

    data = {
        'clt': clt,
    }
    return render(request, 'page/dashboard/createproject.html', data)

def newusetask(request):
    return render(request, 'page/dashboard/addusertache.html')

def connexion(request):
    return render(request, 'page/dashboard/connexion.html')

def sendregister(request):
    #postdata = json.loads(request.body.decode('utf-8'))

    isSucces = False
    # compt = 1 
    # while compt < 10000000:
    #     compt+=1

    file = request.POST.get('file')
    titre = request.POST.get('titre')
    description = request.POST.get('description')
    client = request.POST.get('client')
    budjet = request.POST.get('budjet')
    dpense = request.POST.get('dpense')
    ddebut = request.POST.get('ddebut')
    dfin = request.POST.get('dfin')
    

    print(titre)
    print(description)
    print(client)
    print(budjet)
    print(dpense)
    print(ddebut)
    print(dfin)
    if ((titre is not None) and (description is not None) ):
        try:
            projet = models.Projet(titre=titre, description=description, client=client, budjet=budjet, cahier_de_charge=file, dpense=dpense, ddebut=ddebut, dfin=dfin)
            projet.save()
            print('okkkkkkkkkkkkkkkkkkkkkk+++++++')

        except Exception as err:
            print(err)
            print('+++++--------++++++++++++++')
            datas={
                'success':False,
                'message':'Error pas d\'enregistrement '
            }

    print("+++++++\n",request.POST['titre'])
    print("+++++++\n",request.FILES['description'])

    return JsonResponse(datas, safe=False)
