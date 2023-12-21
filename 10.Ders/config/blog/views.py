from django.shortcuts import render
from .models import *



def home_page(request):
    evler = Houses.objects.filter(is_active = True)
    return render(request,'index.html',{'houses' :evler})


def house_detail(request,detail_slug):
    home = Houses.objects.get(slug= detail_slug)
    
    return render(request,'detay-house.html', {'ev':home})
