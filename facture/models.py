from django.db import models
from django.db.models.signals import post_save
from devis.models import Devis
from client.models import Client
from django.dispatch import receiver
# Create your models here.

class Facture(models.Model):
    devis = models.OneToOneField(Devis,null = True, blank = True ,on_delete = models.CASCADE)
    # client = models.OneToOneField(Client,null = True, blank = True ,on_delete = models.CASCADE)


    


class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture,null = True, blank = True, on_delete = models.CASCADE)
    description = models.CharField(max_length = 100)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    
  
    
@receiver(post_save, sender=Facture)
def createfacture(sender, instance, created, **kwargs):
    if created:
        for lignedevis in instance.devis.lignedevis_set.all() :
            LigneFacture.objects.create(
                facture= instance,
                description = lignedevis.description,
                quantity = lignedevis.quantity,
                price = lignedevis.price,
            )
post_save.connect(createfacture, sender=Facture)
            