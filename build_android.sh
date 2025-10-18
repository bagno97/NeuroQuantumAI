#!/bin/bash
# build_android.sh
# Skrypt do automatycznego budowania aplikacji NeuroQuantumAI na Androida
# Autor: NeuroQuantumAI Team
# Data: Październik 2025

set -e  # Zatrzymaj skrypt przy pierwszym błędzie

echo "=== Rozpoczynam proces budowania aplikacji NeuroQuantumAI na Androida ==="

# Sprawdź czy Python jest zainstalowany
if ! command -v python3 &> /dev/null; then
    echo "BŁĄD: Python3 nie jest zainstalowany. Zainstaluj Python3 i spróbuj ponownie."
    exit 1
fi

# Sprawdź wersję Pythona (powinien być 3.7+)
PYTHON_VERSION=$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')
PYTHON_MAJOR=$(echo $PYTHON_VERSION | cut -d. -f1)
PYTHON_MINOR=$(echo $PYTHON_VERSION | cut -d. -f2)

if [ "$PYTHON_MAJOR" -lt 3 ] || ([ "$PYTHON_MAJOR" -eq 3 ] && [ "$PYTHON_MINOR" -lt 7 ]); then
    echo "OSTRZEŻENIE: Zalecana wersja Python to 3.7+. Twoja wersja to $PYTHON_VERSION"
    echo "Czy chcesz kontynuować mimo to? (t/n)"
    read answer
    if [ "$answer" != "t" ]; then
        echo "Przerwano budowanie."
        exit 1
    fi
fi

# Sprawdź czy wirtualne środowisko istnieje, jeśli nie, stwórz je
if [ ! -d "venv" ]; then
    echo "Tworzę wirtualne środowisko Python..."
    python3 -m venv venv
fi

# Aktywuj wirtualne środowisko
echo "Aktywuję wirtualne środowisko..."
source venv/bin/activate

# Zainstaluj wymagane pakiety narzędziowe (bez Kivy na hoście)
echo "Instaluję narzędzia do budowania (buildozer, cython itp.)..."
export PIP_DISABLE_PIP_VERSION_CHECK=1
pip install --upgrade pip wheel
pip install setuptools==65.5.1 packaging
pip install buildozer==1.5.0 cython==0.29.36

# Sprawdź czy plik buildozer.spec istnieje, jeśli nie, utwórz go
if [ ! -f "buildozer.spec" ]; then
    echo "Nie znaleziono pliku buildozer.spec. Inicjalizuję buildozer..."
    buildozer init
fi

# Przygotowanie dla Samsung Galaxy A35 5G
echo "Przygotowuję budowanie dla Samsung Galaxy A35 5G..."
echo "Upewnianie się, że wszystkie zależności systemowe są zainstalowane..."
sudo apt-get update
sudo apt-get install -y build-essential libltdl-dev libffi-dev libssl-dev autoconf automake libtool pkg-config
sudo apt-get install -y openjdk-17-jdk openjdk-17-jre

# Dodatkowe sprawdzenia dla Samsung Galaxy A35 5G
echo "Sprawdzanie konfiguracji dla Samsung Galaxy A35 5G..."
if ! grep -q "android.archs = arm64-v8a" buildozer.spec; then
    echo "Aktualizuję architekturę dla Samsung Galaxy A35 5G..."
    sed -i 's/android.archs = .*/android.archs = arm64-v8a/g' buildozer.spec
fi

# Buduj APK
echo "Rozpoczynam budowanie aplikacji Android dla Samsung Galaxy A35 5G..."

# Zablokuj pkg-config/sdl2-config z hosta, które psują cross-compilację (dodają -I/usr/include itp.)
echo "Wyłączam hostowe pkg-config i sdl2-config na czas kompilacji (cross-compile safe)"
export PKG_CONFIG=/bin/false
export PKG_CONFIG_PATH=
# Ogranicz ścieżkę pkg-config do pustego katalogu, by nie znajdywał hostowych *.pc
export PKG_CONFIG_LIBDIR="$(pwd)/.empty-pkgconfig"
mkdir -p "$PKG_CONFIG_LIBDIR"
# Zablokuj sdl2-config i pochodne
export SDL2_CONFIG=/bin/false
export SDL2_MIXER_CONFIG=/bin/false
export SDL2_TTF_CONFIG=/bin/false
export SDL2_IMAGE_CONFIG=/bin/false

# Wyczyść poprzednie buildy, aby wymusić przebudowę Kivy z poprawnymi flagami
buildozer android clean || true

# Uruchom kompilację z logowaniem do pliku
mkdir -p build_logs
ts=$(date +%Y%m%d_%H%M%S)
LOG_FILE="build_logs/build_${ts}.log"
echo "Log kompilacji: $LOG_FILE"
buildozer -v android debug 2>&1 | tee "$LOG_FILE"

# Sprawdź czy plik APK został utworzony
if [ -f "bin/neuroquantumai-0.2-debug.apk" ]; then
    echo "=== SUKCES! ==="
    echo "Aplikacja została zbudowana pomyślnie dla Samsung Galaxy A35 5G."
    echo "Plik APK znajduje się w: bin/neuroquantumai-0.2-debug.apk"
    echo "Aby zainstalować aplikację na Samsung Galaxy A35 5G:"
    echo "1. Przenieś plik APK na urządzenie (przez USB, email lub chmurę)"
    echo "2. Przejdź do Ustawienia > Biometria i zabezpieczenia > Zainstaluj nieznane aplikacje"
    echo "3. Wybierz aplikację, którą użyjesz do instalacji (np. Menedżer plików)"
    echo "4. Włącz przełącznik 'Zezwalaj z tego źródła'"
    echo "5. Otwórz plik APK i postępuj zgodnie z instrukcjami instalacji"
    echo ""
    echo "Pamiętaj, że Samsung Galaxy A35 5G ma zabezpieczenia Knox, które mogą wymagać dodatkowych uprawnień."
else
    echo "=== BŁĄD! ==="
    echo "Coś poszło nie tak podczas procesu budowania. Sprawdź logi w katalogu .buildozer/"
    exit 1
fi

# Deaktywuj wirtualne środowisko
deactivate

exit 0