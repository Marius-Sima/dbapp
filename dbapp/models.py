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

    def __str__(self):
        return self.user.username

