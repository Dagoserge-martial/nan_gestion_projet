from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
import requests
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from  django.contrib.auth import  authenticate ,login ,logout
from . import models

# Create your views here.

def home(request):

    url = "https://api.github.com/users/Dagoserge-martial/repos"

    response = requests.get(url)

    resultat = response.text
    contenu = json.loads(resultat)

    print(response.status_code)
    
    if response.status_code == 200:
        for i in range(len(contenu)):
            nom_repos = contenu[i]["name"]
            #nom_repos = 'en Asie'

            #Vérifier si le repos exist
            try :
                nom_rep = models.Projet.objects.filter(titre=nom_repos)[:1].get()
                exist_proj = False
                print('Le projet <<', nom_rep,'>> existe deja !')

                #Recupérer les commentaires en fonction du repos
                url_comit = 'https://api.github.com/repos/Dagoserge-martial/{}/commits'.format(nom_repos)

                resp = requests.get(url_comit)
                if resp.status_code == 200:
                    sult = resp.text
                    resultt = json.loads(result)
                    print('+++++++++', resp.status_code)
                else:
                    print('L api ne fonctionne pas !')
            except:
                exist_proj = True
                print('nooooooooo')

            #Enregistrer le repos s'il n'existe pas
            if exist_proj:
                print('Je scrap ****', nom_repos)
            #print(json.dumps(contenu, indent=4) )
            #print(nom_repos)


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
        'dash': "active",
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
    projet= models.Projet.objects.all()
    clent = models.Client.objects.all()
    projt = models.Projet.objects.filter(isTermine=True)
    data = {
        'projets': 'active',
        'projet': projet,
        'client': clent,
        'projt': projt,
    }
    return render(request, 'page/dashboard/list_projet.html', data)

def list_user(request):
    profile_all = models.TacheUser.objects.all()
    users = models.User.objects.all()
    nbuser = users.count()-1
    # proj = models.TacheUser.objects.filter(statut=True).filter( projet = models.User.user_tachecommit )
    # print(proj)
    useT = users.count()
    print(useT)

    data = {
        'myuser': 'active',
        'profile_all': profile_all,
        'users': users,
        'useT': useT,
        #'proj':proj,
    }
    return render(request, 'page/dashboard/users.html', data)

def detailuser(request, id):
    profil = models.User.objects.get(pk=id)
    #profil = models.User.objects.get(id=4)
    nb = profil.user_tachecommit.all().filter(tache = models.Tache_projet.objects.filter(isTermine=True))
    projetp = profil.user_tachecommit.all()
    nbpt = profil.user_tachecommit.all().count()
    print(nbpt)
    data = {
        'profil':profil,
        'nbpt':nbpt,
        'nb':nb,
        'projetp':projetp,
    }
    #{% url 'detailuser' home.pk %}
    return render(request, 'page/dashboard/detail_user.html', data)


def projetdetail(request, id):
    projet = models.Projet.objects.get(pk=id)
    projt = models.Projet.objects.filter(isTermine=True)
    taches = models.TacheUser.objects.filter(statut=True)
    tch = projet.tache_projet.all().count()
    print(tch)

    data = {
        'projet':projet,
        'projt':projt,
        'taches':taches
    }
    return render(request, 'page/dashboard/projetdetail.html', data)

def commit(request):
    return render(request, 'page/dashboard/commit.html')

def commits(request):
    user_comit = models.User.objects.all()
    commit_date =  models.Commit.objects.distinct().order_by('-date_update')
    #nb = user_comit.user_commit.all().filter(tache = models.Tache_projet.objects.filter(isTermine=True))

    print(commit_date)
    
    data = {
        'user_comit': user_comit,
        'commit_date': commit_date,
    }
    return render(request, 'page/dashboard/commits.html', data)

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
