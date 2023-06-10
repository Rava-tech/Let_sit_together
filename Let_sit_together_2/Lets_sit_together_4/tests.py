from django.test import TestCase
from django.test import Client
import pytest
from django.urls import reverse
from Let_sit_together_4 import models
from Let_sit_together_4.models import Restauracja, Klient, Rezerwacja

@pytest.fixture
def client():
    # Utwórz klienta testowego
    client = Client()
    return client

def test_home(client):
    # Testuj widok home
    response = client.get('/')
    assert response.status_code == 200
    assert 'Strona główna' in response.content.decode('utf-8')

def test_search_view(client):
    # Testuj widok search
    response = client.get('/search/')
    assert response.status_code == 200
    assert 'Wyszukiwarka' in response.content.decode('utf-8')

def test_register(client):
    # Testuj widok rejestracji
    response = client.get('/register/')
    assert response.status_code == 200
    assert 'Rejestracja' in response.content.decode('utf-8')

def test_login_view(client):
    # Testuj widok logowania
    response = client.get('/login/')
    assert response.status_code == 200
    assert 'Logowanie' in response.content.decode('utf-8')

class MyAppTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.restauracja = Restauracja.objects.create(nazwa="Restauracja A")
        self.klient = Klient.objects.create(imie="John", nazwisko="Doe")
        self.rezerwacja = Rezerwacja.objects.create(
            klient=self.klient,
            restauracja=self.restauracja,
            data="2023-05-30",
            liczba_osob=4
        )

    def test_strona_glowna(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Witaj w aplikacji")

    def test_dodaj_rezerwacje(self):
        response = self.client.post(reverse('dodaj_rezerwacje'), {
            'klient_id': self.klient.id,
            'restauracja_id': self.restauracja.id,
            'data': '2023-06-05',
            'liczba_osob': 3
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('wyniki'))

        # Sprawdź czy rezerwacja została dodana do bazy danych
        rezerwacja = Rezerwacja.objects.get(klient=self.klient)
        self.assertEqual(rezerwacja.restauracja, self.restauracja)
        self.assertEqual(rezerwacja.data, '2023-06-05')
        self.assertEqual(rezerwacja.liczba_osob, 3)