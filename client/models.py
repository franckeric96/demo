from django.db import models
from .make_slug import unique_slug_generator
from django.db.models.signals import pre_save
from django.dispatch import receiver



# Create your models here.

class Client(models.Model):
    
    nom=models.CharField(max_length=200,null=True)
    prenoms=models.CharField(max_length=200,null=True)
    ville=models.CharField(max_length=200,null=True)
    pays=models.CharField(max_length=200,null=True)
    fonction=models.CharField(max_length=200,null=True)

    telephone=models.CharField(max_length=50,null=True)
    email=models.EmailField(null=True)
    date_creation=models.DateTimeField(auto_now_add=True,null=True)
    archive = models.BooleanField(default=False)
    slug = models.SlugField(unique=True,max_length = 250, null = True, blank = True)


    
    

    def __str__(self):
        return self.nom




@receiver(pre_save, sender=Client)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

