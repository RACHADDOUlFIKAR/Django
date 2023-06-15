from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from operator import itemgetter
from .models import Utilisateur
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as logouts
from django.contrib import messages

# Create your views here.

 

def conx(request):
    
    if request.method == 'POST':
        email = request.POST['mail']
        passwod = request.POST['psswd']
        user = authenticate(username=email,password=passwod)
        if user is not None:
            
                login(request, user)
                request.session['username'] = email
                name = request.session['username']
                
                #context = {
                   # 'name' : name
               # }
                return redirect('/home',name)
        else:
            messages.error(request,"Bad credentiels")
            return render(request, "session.html")

    return render (request,"session.html")

def register(request):
    user = Utilisateur()
    if request.method == "POST":
        user.name=request.POST["name"]
        user.email=request.POST["mail"]
        user.cin=request.POST["cin"]
        user.password=request.POST["psswd"]
        user.save()
        return render(request, "session.html")
    return render (request,"registration.html")

def logout(request):
    if request.method == 'POST':
        logouts(request)
        del request.session['username']
        return render(request, "session.html")
    return redirect('connexion')