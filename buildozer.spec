[app]

# buildozer.spec
# Konfiguracja kompilacji aplikacji neuronowo-kwantowej AI na Androida
# Więcej opcji: https://buildozer.readthedocs.io/en/latest/specifications.html

title = NeuroQuantumAI


# Unikalna nazwa paczki (zmień na własną domenę)
package.name = neuroquantumai
package.domain = com.example


# Główne źródła - WSZYSTKIE pliki aplikacji!
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif,bmp,kv,atlas,json,txt,md,sh,spec,Json,log,cfg,ini,yaml,yml,xml,csv,dat


# Ikona aplikacji
icon.filename = %(source.dir)s/icon.png


# Główny plik startowy
source.include_entrypoint = True


# Typ kompilacji: debug/release
version = 0.2
# Dodaj zależności pip wymagane przez AI - zoptymalizowane dla Samsung Galaxy A35 5G
# ROZSZERZONE ZALEŻNOŚCI - pełna funkcjonalność AI + telefon!
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3==3.9.17,hostpython3==3.9.17,setuptools,kivy==2.1.0,requests,plyer,pillow==8.4.0,urllib3,certifi,pyjnius,android,sqlite3,openssl,libffi,flask


# Target Android
osx.kivy_version = 2.3.0
orientation = portrait


# Minimalna wersja Androida - dostosowana do Samsung Galaxy A35 5G
android.minapi = 26
android.api = 34
android.sdk = 34
android.ndk = 25b
android.archs = arm64-v8a


# PEŁNE UPRAWNIENIA ANDROID - AI ma dostęp do wszystkich funkcji telefonu!
android.permissions = INTERNET, CAMERA, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, READ_CONTACTS, WRITE_CONTACTS, SEND_SMS, RECEIVE_SMS, READ_SMS, CALL_PHONE, READ_CALL_LOG, WRITE_CALL_LOG, READ_PHONE_STATE, MODIFY_AUDIO_SETTINGS, ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE, BLUETOOTH, BLUETOOTH_ADMIN, VIBRATE, WAKE_LOCK, SYSTEM_ALERT_WINDOW, ACCESS_NOTIFICATION_POLICY, BIND_NOTIFICATION_LISTENER_SERVICE, READ_PHONE_NUMBERS, ANSWER_PHONE_CALLS, USE_FINGERPRINT, FOREGROUND_SERVICE, REQUEST_INSTALL_PACKAGES, MANAGE_EXTERNAL_STORAGE, ALL_FILES_ACCESS, READ_MEDIA_IMAGES, READ_MEDIA_VIDEO, READ_MEDIA_AUDIO

[buildozer]
log_level = 2
warn_on_root = 1
color = always
verbose = 2

[app.android]

# Dodatkowe zależności pip (jeśli potrzebujesz)
# p4a.local_recipes = /workspaces/NeuroQuantumAI/p4a_recipes
# p4a.branch = master

# Wyczyść środowisko kompilacji z systemowych flag host'a
p4a.setuppy_flags = --avoid-system-libs
p4a.hook_dir = 
p4a.build_dir = 
p4a.clean_builds = True

# Konfiguracja pod Samsung Galaxy A35 5G
android.allow_backup = True
android.presplash_color = #ffffff
android.presplash.resize = False
android.entrypoint = org.kivy.android.PythonActivity
android.accept_sdk_license = True

# Optymalizacje dla Galaxy A35 5G
android.gradle_dependencies = androidx.work:work-runtime:2.7.1

# Całkowita izolacja środowiska cross-compilation - unikanie konfliktów z systemowymi nagłówkami
# p4a.environment variables with SDL2 macro fixes
p4a.environment = 
    PATH=:$PATH,
    C_INCLUDE_PATH=,
    CPLUS_INCLUDE_PATH=,
    CPATH=,
    LIBRARY_PATH=,
    LD_LIBRARY_PATH=,
    PKG_CONFIG_PATH=,
    CFLAGS="-D__GNUC_PREREQ(maj,min)=1 -D__glibc_clang_prereq(maj,min)=0",
    CPPFLAGS="-D__GNUC_PREREQ(maj,min)=1 -D__glibc_clang_prereq(maj,min)=0",
    CXXFLAGS=--sysroot=${ANDROIDNDK}/toolchains/llvm/prebuilt/linux-x86_64/sysroot -nostdinc,
    LDFLAGS=--sysroot=${ANDROIDNDK}/toolchains/llvm/prebuilt/linux-x86_64/sysroot

# Wyłącz systemowe ścieżki include dla wszystkich etapów kompilacji
android.add_compile_options = --sysroot=$(ANDROID_NDK)/toolchains/llvm/prebuilt/linux-x86_64/sysroot

# Dodatkowe ustawienia dla p4a żeby uniknąć problemów cross-compilation  
p4a.bootstrap = sdl2
p4a.setup_py_args = --avoid-system-libs
