from django.db import models

class Restauracja(models.Model):
    nazwa = models.CharField(max_length=100)
    lokalizacja = models.CharField(max_length=100)
    liczba_miejsc = models.IntegerField()

class Klient(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    email = models.EmailField()
    telefon = models.CharField(max_length=20)

class Rezerwacja(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
    data = models.DateField()
    liczba_osob = models.IntegerField()

class Klient_Restauracja(models.Model):
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)
    restauracja = models.ForeignKey(Restauracja, on_delete=models.CASCADE)
