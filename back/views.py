from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.db import models
from back.models import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404
 
def index(request):
    context ={}
    
    if request.session['userlogin']=='OK':
        vCard = Informationvcard.objects.all()
        context = {"vCard":vCard}
        return render(request, "index.html", context)
       
        
    else : 
        return render(request, "loginHome.html", context)
        
        
def liste(request):
    context ={}
    if request.session['userlogin']=='OK':
        if request.method=="GET":
            idO=request.GET.get('idO')
            if idO is None:
                vCard = Informationvcard.objects.all()
            
            else :
                vCard = Informationvcard.objects.filter(organisme_id=idO)
            
        context = {"vCard":vCard}   
        return render(request, "liste.html", context)
    else:
        return render(request, "loginHome.html", context)
    
def detailCard(request):
    context = {}
    if request.session['userlogin']=='OK':
        if request.method=="GET":
            idC=request.GET.get('idC')
            organisme = Organisme.objects.all()
            detailCard = Informationvcard.objects.filter(id=idC)
            context = {'detailCard': detailCard,'idC':idC,'organisme':organisme}
            
        return render(request,"detailCard.html", context)
    else:
        return render(request, "loginHome.html", context)

    
def login(request):
    context ={}
    request.session['userlogin']="";
    if request.session['userlogin']=='OK':
        vCard = Informationvcard.objects.all()
        context = {"vCard":vCard}
        return render(request, "index.html", context)
    else:
        return render(request, "loginHome.html", context)
     
     
def parOrganisme(request):
    context ={}
    if request.session['userlogin']=='OK':
        parOrganisme = Organisme.objects.all()
        context = {"parOrganisme":parOrganisme}   
        return render(request, "parOrganisme.html", context)
    else:
  
        return render(request, "loginHome.html", context)        
    
def connexion(request):
    context = {}
    if request.method=='POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            request.session['userlogin'] = 'OK'
            vCard = Informationvcard.objects.all()
            context = {"vCard":vCard}
            return render(request, "index.html", context)
            
        else:
            
            return render(request, "loginHome.html", context)
            
            
def logout(request):
    context ={}
    request.session['userlogin'] = False
    return render(request, "loginHome.html", context)
   