[app]

# Nazwa aplikacji (widoczna na urządzeniu)
title = NeuroQuantumAI

# Nazwa pakietu (unikalna, odwrotna notacja domenowa)
package.name = neuroquantumai
package.domain = org.bagno97

# Plik startowy
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt

# Wersja aplikacji
version = 1.0.0

# Zależności Pythona (z requirements.txt)
requirements = python3,kivy,plyer,requests,flask,numpy,pyjnius,android

# Ikona aplikacji (opcjonalnie - stwórz plik icon.png 512x512px)
#icon.filename = %(source.dir)s/icon.png

# Ekran powitalny (opcjonalnie)
#presplash.filename = %(source.dir)s/presplash.png

# Orientacja (landscape, portrait, all)
orientation = portrait

# Usługi w tle (opcjonalnie)
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

# Wsparcie dla full-screen
fullscreen = 0

# Uprawnienia Android (KLUCZOWE dla funkcji telefonu!)
android.permissions = INTERNET,CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,SEND_SMS,READ_SMS,RECEIVE_SMS,CALL_PHONE,READ_PHONE_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,BLUETOOTH,BLUETOOTH_ADMIN,VIBRATE,WAKE_LOCK

# Funkcje Android
android.features = android.hardware.camera,android.hardware.location.gps

# API Android (28 = Android 9.0, 33 = Android 13)
android.api = 33
android.minapi = 21
android.ndk = 25b

# Architektura procesora
android.archs = arm64-v8a,armeabi-v7a

# Tryb release (0 = debug, 1 = release)
android.release_artifact = apk
#android.debug_artifact = apk

# Klucz do podpisywania APK (dla release)
#android.keystore = ~/keystores/neuroquantum.keystore
#android.keystore_alias = neuroquantumalias

# Bootstrap (wybierz sdl2 dla Kivy)
p4a.bootstrap = sdl2

# Lokalne repozytoria (opcjonalnie)
#p4a.local_recipes = ./p4a-recipes

# Whitelist dla modułów
android.whitelist = lib-dynload/termios.so

# Czy kompilować w trybie debug
log_level = 2
warn_on_root = 1

[buildozer]

# Logi
log_level = 2
warn_on_root = 1