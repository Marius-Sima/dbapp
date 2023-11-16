from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class cerere_de_finantare(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numele_solicitantului = models.CharField(max_length=255)
    titlul_proiectului = models.TextField()
    programe_choices = [
        ('cultura','Cultura'),
        ('mass_media','Mass-Media'),
        ('educatie','Educatie'),
        ('spiritualitate','Spiritualitate si Traditie'),
        ('societate','Societate Civila')]
    programe = models.CharField(max_length=30, choices=programe_choices)
    locul_derulare = models.TextField(help_text="Adresa, cod postal, Regiune, Localitate, Tara")
    #perioada_incepere = models.DateTimeField()
    #perioada_incheiere = models.DateField()
    def __str__(self):
        return f'Numele Solicitantului {self.numele_solicitantului}, titlul proiectului {self.titlul_proiectului}, locul de derulare {self.locul_derulare}'

    class Meta:
        db_table = "Cerere_de_Finantare"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

