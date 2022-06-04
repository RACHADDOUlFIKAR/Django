from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Auteur
from .forms import AuteurForm
# Create your views here.


def all_authors(request):
      aut_data=Auteur.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  aut_data
            else:
                  aut_data=Auteur.objects.filter(Nom =Search)

      countdt = Auteur.objects.count()
      return render(request,"Auteur/aut.html",{'aut_data':aut_data,'countdt': countdt})

def create_author(request):
      form=AuteurForm
      if request.method == 'POST':
            form=AuteurForm(request.POST)
            if form.is_valid():
                  form.save()
            return redirect('/auteurs')  # 4
      else:
       return render(request,"Auteur/new_author.html",{'form':form})

def update_author(request,Id):
      aut_data=Auteur.objects.get(Id=Id)
      form=AuteurForm(instance=aut_data)
      if request.method == 'POST':
            form=AuteurForm(request.POST,instance=aut_data)
            if form.is_valid():
                  form.save()
            return redirect('/auteurs')  # 4
      else:
       return render(request,"Auteur/update_author.html",{'form':form})

def delete_author(request,Id):
      aut_data=Auteur.objects.get(Id=Id)
      aut_data.delete()
      return redirect('/auteurs')