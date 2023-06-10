from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Klient, Restauracja, Rezerwacja


def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # Dodaj komunikat o sukcesie
            messages.success(request, 'Rejestracja zakończona pomyślnie. Witamy!')
            return redirect('welcome')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def search(request):
    places = request.GET.get('places')
    distance = request.GET.get('distance')

    # Przetwarzanie wyszukiwania i wykonanie odpowiednich działań
    # ...

    return render(request, 'search.html')

def welcome_view(request):
    return render(request, 'welcome.html')

def login_view(request):
    if request.method == 'POST':
        # Logika uwierzytelniania użytkownika
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Przekierowanie użytkownika na stronę główną
            return redirect('welcome.html')  # 'home.html' to nazwa widoku dla strony głównej
        else:
            # Obsługa błędnego uwierzytelniania
            pass
    else:
        # Renderowanie formularza logowania
        pass

def profile_view(request):
    # Logika wyświetlania profilu użytkownika
    return render(request, 'profile.html', {'user': request.user})

def logout_view(request):
    logout(request)
    return redirect('home.html')

def search_map(request):
    if request.method == 'POST':
        # Przetwarzanie danych z formularza
        radius = request.POST.get('radius')  # Przykładowe pole formularza

        # Przygotowanie kontekstu dla szablonu
        context = {
            'radius': radius,
        }

        return render(request, 'map.html', context)
    else:
        return render(request, 'search.html')

def search_view(request):
    # Przetwarzanie danych i przygotowanie wyników
    # ...
    return redirect('search_results')

def dodaj_rezerwacje(request):
    # Pobierz dane z formularza
    klient_id = request.POST.get('klient_id')
    restauracja_id = request.POST.get('restauracja_id')
    data = request.POST.get('data')
    liczba_osob = request.POST.get('liczba_osob')

    # Utwórz obiekty klienta i restauracji
    klient = Klient.objects.get(id=klient_id)
    restauracja = Restauracja.objects.get(id=restauracja_id)

    # Utwórz nową rezerwację
    rezerwacja = Rezerwacja.objects.create(
        klient=klient,
        restauracja=restauracja,
        data=data,
        liczba_osob=liczba_osob
    )

    # Przekieruj użytkownika lub wykonaj inne operacje

    return HttpResponseRedirect('/results/')
