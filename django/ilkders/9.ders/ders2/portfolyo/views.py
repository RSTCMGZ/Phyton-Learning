from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    return render(request,'index.html')


 
def projeler(request):
        projelerim = Projelerim.objects.all()
        return render(request,'projeler.html', {'projelerim':projelerim})

def proje_detay(request,detay_slug):
   
        proje = Projelerim.objects.get(slug= detay_slug)
        return render(request,'projeler.html', {'projelerim':proje})
def category(request,category_slug):
       cat= Category.objects.get(slug = category_slug)
       projelerim = cat.projelerim_set.all()
       return render(request,'projeler.html',{'projelerim':projelerim})


