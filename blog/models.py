from django.conf import settings
from django.db import models

class Lieu(models.Model):
    id_lieu = models.CharField(max_length=100, primary_key=True)
    disponibilité = models.CharField(max_length=20, choices=[('disponible', 'Disponible'), ('occupé', 'Occupé')])
    photo = models.ImageField(upload_to='lieus/')
    def __str__(self):
        return self.id_lieu
 
 
class Livre(models.Model):
    id_livre = models.CharField(max_length=100, primary_key=True)
    statut = models.CharField(max_length=20, choices=[('emprunté', 'Emprunté'), ('disponible', 'Disponible')])
    genre = models.CharField(max_length=20)
    auteur = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='livres/')
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.id_livre
    

