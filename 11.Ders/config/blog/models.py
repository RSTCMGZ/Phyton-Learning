from django.db import models
from autoslug import AutoSlugField

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length = 100)
    image = models.FileField(upload_to='profile_pic')
    description = models.TextField()
    position = models.CharField(max_length = 50)

    is_active = models.BooleanField(default = True)

    slug = AutoSlugField(populate_from = 'name',unique = True)

    def __str__(self):
        return self.name

class Houses(models.Model):
    title = models.CharField(max_length = 50,verbose_name='Evin adı:')
    image = models.ImageField(upload_to='houses',verbose_name='Evin resmi:')
    description = models.TextField(verbose_name = 'Evin acıklaması')
    is_active = models.BooleanField(default = True,verbose_name='Satışta mı:')

    owner = models.ForeignKey(Profile, on_delete =models.CASCADE , null=True)

    slug = AutoSlugField(populate_from='title',unique = True)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Ev'
        verbose_name_plural = 'Evler'





# Bir model yazacaksınız.
# Bir kişi modeli oluşturulacak. Kişinin adı, Resmi, Açıklaması,şirkettiki görevi,one to mant baglantısı ise kişinin yaptığı evleride görmek istiyorum.(Foringkey)