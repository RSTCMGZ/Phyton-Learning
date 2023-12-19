from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=150)

    slug = models.SlugField(unique = True,null=True,blank=True)

    is_active = models.BooleanField(default = True)
    
    created_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    update_time = models.DateTimeField(blank=True,null=True,auto_now=True)
    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name) 
        super(Category,self).save(*args, **kwargs)


class Projelerim(models.Model):
    name = models.CharField(max_length = 150)
    img = models.CharField(max_length = 200)
    description = models.TextField()
    slug = models.SlugField(unique = True, null=True,blank=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    
    is_active = models.BooleanField(default = True)

    created_time = models.DateTimeField(blank=True,null=True,auto_now_add=True)
    update_time = models.DateTimeField(blank=True,null=True,auto_now=True)

    def __str__(self):
        return self.name
    def save(self,*args, **kwargs):
        self.slug = slugify(self.name) 
        super(Projelerim,self).save(*args, **kwargs)
