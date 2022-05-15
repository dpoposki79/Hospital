from django.db import models
import random
from datetime import timedelta
from django.utils.timezone import now

class Doktori(models.Model):
    Ime = models.CharField(max_length=50) 
    Prezime = models.CharField(max_length=50) 
    Telefon = models.CharField(max_length=50) 
    Email = models.CharField(max_length=50) 
    Titula = models.CharField(max_length=50) 
    NaKoeOddelenie = models.CharField(max_length=50) 
    PoleSpecijalizacija = models.CharField(max_length=50) 
    Redoven = models.BooleanField() 
    Specijalist = models.BooleanField()
    Faksimil = models.IntegerField(unique=True)
    GodiniIskustvo = models.IntegerField()
    Plata = models.IntegerField()
    Rakovoditel = models.BooleanField()

class Pacienti(models.Model):
    Ime = models.CharField(max_length=50) 
    Prezime = models.CharField(max_length=50) 
    Telefon = models.CharField(max_length=50) 
    Email = models.CharField(max_length=50) 
    DataRaganje = models.DateField() 
    EMBG = models.CharField(max_length=50, unique=True)
    Pol = models.CharField(max_length=10) 
    Krvodaritel = models.BooleanField() 
    KrvnaGrupa = models.CharField(max_length=10)
    Osiguruvanje = models.BooleanField()
    Hronicni = models.BooleanField()
    Alergii = models.BooleanField()
    HronicniBolesti = models.TextField(null=True, blank=True)

class Oddeli(models.Model):
    Ime = models.CharField(max_length=50) 
    Kapacitet = models.IntegerField()
    PomosenPersonal = models.IntegerField()


 
class Hospitalizacija(models.Model):
    Pacient= models.ForeignKey(Pacienti, on_delete=models.CASCADE, null=True, blank=True)
    Doktor = models.ForeignKey(Doktori, on_delete=models.CASCADE, null=True, blank=True)
    Oddel = models.ForeignKey(Oddeli, on_delete=models.CASCADE, null=True, blank=True)
    DataHospitalizacija = models.DateField()
    Dijagnoza = models.TextField(null=True, blank=True) 
    Rezultati = models.TextField(null=True, blank=True)
    BrSoba = models.IntegerField(null=True, blank=True) 
    BrojKrevet = models.IntegerField(null=True, blank=True) 
    Terapija = models.CharField(max_length=50,null=True, blank=True) 
    Hospitaliziran = models.BooleanField()

class Termin(models.Model):
    Pacient= models.ForeignKey(Pacienti, on_delete=models.CASCADE, null=True, blank=True)
    Doktor = models.ForeignKey(Doktori, on_delete=models.CASCADE, null=True, blank=True)
    Oddel = models.ForeignKey(Oddeli, on_delete=models.CASCADE, null=True, blank=True)
    Termin = models.DateTimeField(null=True, blank=True)
    Simptomi = models.TextField(null=True, blank=True) 
    Prioritet = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if self.Prioritet == True:
            za_kolku_vreme  = random.randint(1, 23)
            random_minuti = random.randint(1, 59)
            self.Termin = now() + timedelta(hours=za_kolku_vreme, minutes=random_minuti)
            super(Termin, self).save(*args, **kwargs)

class Pregledi(models.Model):
    Pacient= models.ForeignKey(Pacienti, on_delete=models.CASCADE, null=True, blank=True)
    Doktor = models.ForeignKey(Doktori, on_delete=models.CASCADE, null=True, blank=True)
    NaKoeOddelenie = models.ForeignKey(Oddeli, on_delete=models.CASCADE, null=True, blank=True)
    DatumPregled = models.DateTimeField()
    Zabeleska = models.TextField(null=True, blank=True) 
    KontrolaZa = models.IntegerField(null=True, blank=True)
    Dijagnoza = models.TextField(null=True, blank=True) 
    Terapija = models.TextField(null=True, blank=True) 
    Upat = models.ForeignKey(Termin, on_delete=models.CASCADE, null=True)