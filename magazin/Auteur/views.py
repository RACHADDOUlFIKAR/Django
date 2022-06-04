from ast import NameConstant
from django.shortcuts import render,redirect
from .models import Auteur
from .forms import AuteurForm
# Create your views here.
def book(request):
      pro_data=product.objects.all()
      if 'Search' in request.GET:
            
            Search=request.GET['Search']
            if Search=="":
                  pro_data
            else:
                  
                  pro_data=product.objects.filter(nom =Search)
      
      countdt = product.objects.count()
      return render(request,"product/book.html",{'prodata':pro_data,'countdt': countdt})
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