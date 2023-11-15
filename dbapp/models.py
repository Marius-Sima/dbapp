from django.db import models
from datetime import datetime

# Create your models here.


class Programe(models.Model):
    cultura = 1
    mass_media = 2
    educatie = 3
    spiritualitate = 4
    societate = 5
    alege = [
        (cultura, "Cultura"),
        (mass_media, "Mass Media"),
        (educatie, "Educatie"),
        (spiritualitate, "Spiritualitate si Traditie"),
        (societate, "Societate Civila"),]

class cerere_de_finantare(models.Model):
    numele_solicitantului = models.CharField(max_length=255)
    titlul_proiectului = models.TextField()
    programe = models.CharField(max_length=2,choices=Programe.alege)
    locul_derulare = models.TextField(help_text="Adresa, cod postal, Regiune, Localitate, Tara")
    #perioada_incepere = models.DateTimeField()
    #perioada_incheiere = models.DateField()

    class Meta:
        db_table = "Cerere_de_Finantare"
