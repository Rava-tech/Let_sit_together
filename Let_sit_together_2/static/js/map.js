// Inicjalizacja mapy
var map = L.map('map').setView([{{ latitude }}, {{ longitude }}], 13);  // Ustawienie centrum mapy na bieżącą lokalizację

// Dodanie warstwy mapy OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
    maxZoom: 18,
}).addTo(map);

// Dodanie okręgu o podanym promieniu
var radius = {{ radius }};
var circle = L.circle([{{ latitude }}, {{ longitude }}], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: radius
}).addTo(map);

if ("geolocation" in navigator) {
    navigator.geolocation.getCurrentPosition(function(position) {
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;

        // Ustawienie centrum mapy na bieżącą lokalizację
        map.setView([latitude, longitude], 13);

        // Dodanie okręgu o podanym promieniu
        var circle = L.circle([latitude, longitude], {
            color: 'red',
            fillColor: '#f03',
            fillOpacity: 0.5,
            radius: radius
        }).addTo(map);
    });
}

document.getElementById('search-button').addEventListener('click', function() {
    // Pobierz dane z formularza
    var radius = document.getElementById('radius-input').value;

    // Utwórz mapę z odpowiednimi ustawieniami
    var map = L.map('map').setView([{{ latitude }}, {{ longitude }}], 13);

    // Dodaj warstwę mapy, np. OpenStreetMap
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors',
        maxZoom: 18,
    }).addTo(map);

    // Dodaj okrąg o podanym promieniu i centrum na bieżącą lokalizację
    var circle = L.circle([{{ latitude }}, {{ longitude }}], {
        color: 'red',
        fillColor: '#f03',
        fillOpacity: 0.5,
        radius: radius
    }).addTo(map);
});




