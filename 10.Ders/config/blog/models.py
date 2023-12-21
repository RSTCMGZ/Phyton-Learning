from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class Houses(models.Model):
    title = models.CharField(max_length = 50, verbose_name = 'Evin adi:' )
    image = models.ImageField(upload_to='houses',  verbose_name = 'Evin resmi:')
    description = models.TextField( verbose_name = 'Evin aciklamasi:')
    is_active = models.BooleanField(default = True)

    slug = AutoSlugField(populate_from='title', unique= True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Ev'
        verbose_name_plural = 'Evler'

# bir model yaz
# Bir kişi modeli oluştur(kart).Profile,kisi,User kullanma isim olarak. Kişinin adı,Resmi,Açıklaması,şirketteki görevi,one to many baglantısı ile kişinin yaptıgı evleri de göster.(Foringkey ekle kişilere)