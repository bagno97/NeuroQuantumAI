[app]

# buildozer.spec
# Konfiguracja kompilacji aplikacji neuronowo-kwantowej AI na Androida
# Więcej opcji: https://buildozer.readthedocs.io/en/latest/specifications.html

title = NeuroQuantumAI


# Unikalna nazwa paczki (zmień na własną domenę)
package.name = neuroquantumai
package.domain = com.example


# Główne źródła
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt


# Ikona aplikacji (opcjonalnie podaj własną ścieżkę)
# icon.filename = %(source.dir)s/data/icon.png


# Główny plik startowy
entrypoint = main.py


# Typ kompilacji: debug/release
version = 0.2
# Dodaj zależności pip wymagane przez AI
requirements = python3,kivy,requests,plyer


# Target Android
osx.kivy_version = 2.3.0
orientation = portrait


# Minimalna wersja Androida
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.archs = armeabi-v7a, arm64-v8a


# Uprawnienia (dodaj kolejne jeśli AI korzysta z funkcji telefonu)
android.permissions = INTERNET, CAMERA, ACCESS_FINE_LOCATION, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1

[app.android]

# Dodatkowe zależności pip (jeśli potrzebujesz)
# p4a.local_recipes = 
# p4a.branch = master
