from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
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
    descriere = models.TextField(help_text="Descrieti proiectul")
    perioada_incepere = models.DateField()
    perioada_incheiere = models.DateField()
    def __str__(self):
        return f'User: {self.user} Numele Solicitantului: {self.numele_solicitantului}, Titlul proiectului: {self.titlul_proiectului}, Locul de derulare {self.locul_derulare}'

    class Meta:
        db_table = "Cerere_de_Finantare"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    uploaded_file = models.FileField(upload_to='user_uploads/', blank=True, null=True)
    bio = models.TextField(blank=True)
    cerere_de_finantare = models.ForeignKey(cerere_de_finantare, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.user.username

class Sesiune(models.Model):
        # acest tabel este menit sa stocheze un interval de timp, de regula, nu mai mult de-o saptamana, poate chiar doua
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    @property
    def is_active(self):
        current_date = timezone.now()
        return self.start_date <= current_date <= self.end_date