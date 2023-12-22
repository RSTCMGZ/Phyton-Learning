from django.shortcuts import render
from .models import *
# Create your views here.


def home_page(request):
    evler = Houses.objects.filter(is_active = True)
    personeller = Profile.objects.filter(is_active = True)

    if request.method == 'POST':
        name = request.POST.get('Name')
        resim = request.POST.get('Resim')
        aciklama = request.POST.get('Aciklama')


    return render(request,'index.html',{
        'houses':evler,
        'personeller':personeller
        })


def house_detail(request,detail_slug):
    home = Houses.objects.get(slug = detail_slug)
   
    return render(request,'detay-house.html',{'ev':home})


def kisi_ev(request,kisi_slug):
    kisi = Profile.objects.get(slug = kisi_slug)
    evler = kisi.houses_set.all()
    # Filtreleme yapılabilir
    # evler = kisi.houses_set.filter(is_active = True)

    context ={
        'kisi':kisi,
        'evler':evler
    }

    return render(request,'kisi_ev.html',context)