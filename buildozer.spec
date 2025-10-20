[app]

# buildozer.spec
# Konfiguracja kompilacji aplikacji neuronowo-kwantowej AI na Androida
# Więcej opcji: https://buildozer.readthedocs.io/en/latest/specifications.html

title = NeuroQuantumAI


# Unikalna nazwa paczki
package.name = neuroquantumai
package.domain = com.neuroquantum


# WSZYSTKIE ŹRÓDŁA - pełna aplikacja AI!
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,json,txt


# Ikona aplikacji
# icon.filename = %(source.dir)s/icon.png


# Główny plik startowy - wersja Android
source.main = main_android_fixed.py


# Wersja aplikacji
version = 1.0


# PEŁNE ZALEŻNOŚCI - wszystkie moduły AI + telefon + samomodyfikacja
requirements = python3,kivy==2.2.0,requests,plyer,pyjnius,android,certifi,urllib3,pillow


# Target Android
osx.kivy_version = 2.3.0
orientation = portrait


# Minimalna wersja Androida - dostosowana do Samsung Galaxy A35 5G
android.minapi = 26
android.api = 34
android.sdk = 34
android.ndk = 25b
android.archs = arm64-v8a


# PEŁNE UPRAWNIENIA ANDROID - AI ma dostęp do WSZYSTKICH funkcji telefonu!
# Zgodnie z phone_interface.py i phone_permissions.json
android.permissions = INTERNET,CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_CONTACTS,WRITE_CONTACTS,SEND_SMS,RECEIVE_SMS,READ_SMS,CALL_PHONE,READ_CALL_LOG,WRITE_CALL_LOG,READ_PHONE_STATE,MODIFY_AUDIO_SETTINGS,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,BLUETOOTH,BLUETOOTH_ADMIN,VIBRATE,WAKE_LOCK,FOREGROUND_SERVICE,READ_MEDIA_IMAGES,READ_MEDIA_VIDEO,READ_MEDIA_AUDIO

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
