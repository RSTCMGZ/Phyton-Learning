from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home_page,name='anasayfa'),
    path('house-detail/<slug:detail_slug>/',house_detail,name='detail_house'),
    path('house/<slug:kisi_slug>',kisi_ev,name='kisiEv'),
]
