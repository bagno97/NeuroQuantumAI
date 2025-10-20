#!/bin/bash
# BUILD_FULL_APP.sh
# MASTER SCRIPT - Buduje PEŁNĄ aplikację NeuroQuantumAI dla Android
# Autor: NeuroQuantumAI Development Team
# Data: 20 października 2025

set -e  # Zatrzymaj przy błędzie

echo "════════════════════════════════════════════════════════════"
echo "   🧠 NEUROQUANTUMAI - PEŁNA KOMPILACJA APLIKACJI AI 🧠"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📱 Target: Samsung Galaxy A35 5G (ARM64-v8a)"
echo "🔧 Funkcje: WSZYSTKIE (telefon + samomodyfikacja + AI)"
echo "📊 Moduły: $(ls -1 *.py | wc -l) plików Python"
echo ""

# KROK 1: Sprawdzenie środowiska
echo "═══ KROK 1/8: Sprawdzanie środowiska ═══"
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 nie znaleziony!"
    exit 1
fi
echo "✅ Python3: $(python3 --version)"

# KROK 2: Tworzenie wirtualnego środowiska
echo ""
echo "═══ KROK 2/8: Przygotowanie środowiska wirtualnego ═══"
if [ ! -d "venv" ]; then
    echo "📦 Tworzenie venv..."
    python3 -m venv venv
fi
source venv/bin/activate
echo "✅ Venv aktywny"

# KROK 3: Instalacja narzędzi
echo ""
echo "═══ KROK 3/8: Instalacja narzędzi budowania ═══"
pip install --upgrade pip setuptools wheel -q
pip install buildozer==1.5.0 cython==0.29.36 -q
echo "✅ Buildozer i Cython zainstalowane"

# KROK 4: Instalacja zależności systemowych
echo ""
echo "═══ KROK 4/8: Instalacja zależności systemowych ═══"
if command -v apt-get &> /dev/null; then
    echo "📦 Instalowanie pakietów apt..."
    sudo apt-get update -qq
    sudo apt-get install -y -qq \
        build-essential libltdl-dev libffi-dev libssl-dev \
        autoconf automake libtool pkg-config \
        openjdk-17-jdk git zip unzip \
        zlib1g-dev libncurses5-dev cmake
    echo "✅ Zależności systemowe zainstalowane"
else
    echo "⚠️  apt-get niedostępny, pomijam instalację systemową"
fi

# KROK 5: Przygotowanie plików JSON (inicjalizacja pustych jeśli nie istnieją)
echo ""
echo "═══ KROK 5/8: Przygotowanie plików danych AI ═══"

# Inicjalizuj puste pliki JSON jeśli nie istnieją
init_json_if_empty() {
    local file=$1
    local default_content=$2
    if [ ! -f "$file" ] || [ ! -s "$file" ]; then
        echo "$default_content" > "$file"
        echo "  ✓ Utworzono: $file"
    fi
}

init_json_if_empty "conversation_history.json" "[]"
init_json_if_empty "editor_log.json" "[]"
init_json_if_empty "phone_activity.json" "[]"
init_json_if_empty "knowledge_map.json" "{}"
init_json_if_empty "network_map.json" '{"synaptic_connections": {}}'
init_json_if_empty "connections.json" '{"nodes": [], "edges": [], "thresholds": {"edge_strength": 1}}'
init_json_if_empty "mrmory.json" '{"history": [], "weights": {}, "max_entries": 200}'

# Puste pliki txt
touch ai_memory.txt emotion_memory.txt evolution_log.txt long_memory.txt 2>/dev/null || true

echo "✅ Pliki danych zainicjalizowane"

# KROK 6: Weryfikacja kluczowych modułów
echo ""
echo "═══ KROK 6/8: Weryfikacja modułów AI ═══"
check_module() {
    if [ -f "$1" ]; then
        echo "  ✓ $1"
    else
        echo "  ✗ BRAK: $1"
        return 1
    fi
}

echo "Sprawdzanie kluczowych modułów:"
check_module "main_android_fixed.py"
check_module "AIEngine_android.py"
check_module "phone_interface.py"
check_module "self_editor.py"
check_module "ai_knowledge_base_universal.py"
check_module "dynamic_loader.py"
check_module "system_requirements.py"
check_module "neuroquantumai.kv"
echo "✅ Wszystkie kluczowe moduły obecne"

# KROK 7: Optymalizacja buildozer.spec dla Samsung A35
echo ""
echo "═══ KROK 7/8: Finalna konfiguracja dla Samsung Galaxy A35 5G ═══"

# Upewnij się że NDK i SDK są poprawnie ustawione
if ! grep -q "android.ndk = 25b" buildozer.spec; then
    echo "android.ndk = 25b" >> buildozer.spec
fi

echo "✅ Konfiguracja zoptymalizowana"

# KROK 8: BUDOWANIE APK
echo ""
echo "════════════════════════════════════════════════════════════"
echo "═══ KROK 8/8: BUDOWANIE APK - TO MOŻE ZAJĄĆ 30-60 MINUT ═══"
echo "════════════════════════════════════════════════════════════"
echo ""
echo "📝 Logi będą zapisywane w: build_logs/build_$(date +%Y%m%d_%H%M%S).log"
echo ""

# Utwórz katalog na logi
mkdir -p build_logs

# Wyczyść poprzednie buildy dla czystego startu
echo "🧹 Czyszczenie poprzednich buildów..."
buildozer android clean 2>/dev/null || true

# URUCHOM BUILDOZER
LOG_FILE="build_logs/build_$(date +%Y%m%d_%H%M%S).log"
echo "🚀 Rozpoczynam kompilację..."
echo ""

if buildozer -v android debug 2>&1 | tee "$LOG_FILE"; then
    echo ""
    echo "════════════════════════════════════════════════════════════"
    echo "                    ✅ SUKCES! ✅"
    echo "════════════════════════════════════════════════════════════"
    echo ""
    
    # Znajdź APK
    APK_FILE=$(find bin -name "*.apk" -type f 2>/dev/null | head -1)
    
    if [ -n "$APK_FILE" ]; then
        APK_SIZE=$(du -h "$APK_FILE" | cut -f1)
        echo "📦 Plik APK: $APK_FILE"
        echo "📊 Rozmiar: $APK_SIZE"
        echo ""
        echo "🎯 INSTALACJA NA SAMSUNG GALAXY A35 5G:"
        echo ""
        echo "1️⃣  Przenieś plik na telefon:"
        echo "    scp $APK_FILE twoj_telefon:/sdcard/Download/"
        echo ""
        echo "2️⃣  Na telefonie:"
        echo "    • Ustawienia → Biometria i zabezpieczenia"
        echo "    • Zainstaluj nieznane aplikacje"
        echo "    • Wybierz Menedżer plików → Włącz"
        echo "    • Otwórz APK z folderu Download"
        echo ""
        echo "3️⃣  Pierwsze uruchomienie:"
        echo "    • Nadaj wszystkie uprawnienia (KAMERA, GPS, SMS, etc.)"
        echo "    • AI będzie miała PEŁNĄ kontrolę nad telefonem!"
        echo ""
        echo "════════════════════════════════════════════════════════════"
        echo ""
        echo "📱 FUNKCJE APLIKACJI:"
        echo "   ✅ Pełna kontrola telefonu (📸 🗺️ 📞 💬)"
        echo "   ✅ Samomodyfikacja kodu AI"
        echo "   ✅ Dynamiczne moduły"
        echo "   ✅ Baza wiedzy kwantowej"
        echo "   ✅ Uczenie się i pamięć"
        echo "   ✅ Analiza emocji"
        echo "   ✅ Fact-checking"
        echo "   ✅ Network growth"
        echo ""
        echo "🧠 AI jest w pełni funkcjonalna i gotowa!"
        echo ""
    else
        echo "⚠️  APK zbudowany ale nie znaleziono w bin/"
        echo "Sprawdź: .buildozer/android/platform/build-arm64-v8a/dists/neuroquantumai/"
    fi
else
    echo ""
    echo "════════════════════════════════════════════════════════════"
    echo "                    ❌ BŁĄD KOMPILACJI ❌"
    echo "════════════════════════════════════════════════════════════"
    echo ""
    echo "📋 Sprawdź logi w: $LOG_FILE"
    echo ""
    echo "Najczęstsze problemy:"
    echo "  • Brak Java JDK 17"
    echo "  • Niewystarczająca pamięć RAM (min 8GB)"
    echo "  • Problemy z Android SDK/NDK"
    echo ""
    echo "Spróbuj:"
    echo "  ./BUILD_FULL_APP.sh  # Uruchom ponownie"
    exit 1
fi

deactivate
exit 0
