#!/bin/bash
# optimize_for_samsung_a35.sh
# Skrypt do optymalizacji konfiguracji buildozer dla Samsung Galaxy A35 5G

echo "Optymalizacja buildozer.spec dla Samsung Galaxy A35 5G..."

# Upewnij się, że buildozer.spec istnieje
if [ ! -f "buildozer.spec" ]; then
    echo "BŁĄD: Plik buildozer.spec nie został znaleziony!"
    echo "Uruchom najpierw 'buildozer init' aby utworzyć ten plik."
    exit 1
fi

# Kopia zapasowa oryginalnego pliku
cp buildozer.spec buildozer.spec.backup

# Aktualizacja konfiguracji Android API i architektury
sed -i 's/android.minapi = .*/android.minapi = 26/' buildozer.spec
sed -i 's/android.api = .*/android.api = 34/' buildozer.spec 2>/dev/null || sed -i '/\[app\]/a android.api = 34' buildozer.spec
sed -i 's/android.sdk = .*/android.sdk = 34/' buildozer.spec
sed -i 's/android.archs = .*/android.archs = arm64-v8a/' buildozer.spec

# Dodaj sekcję [app.android] jeśli nie istnieje
if ! grep -q "\[app.android\]" buildozer.spec; then
    echo "" >> buildozer.spec
    echo "[app.android]" >> buildozer.spec
    echo "" >> buildozer.spec
fi

# Dodaj optymalizacje dla Samsung Galaxy A35 5G
if ! grep -q "android.allow_backup" buildozer.spec; then
    sed -i '/\[app.android\]/a \
# Konfiguracja pod Samsung Galaxy A35 5G\
android.allow_backup = True\
android.presplash_color = #ffffff\
android.presplash.resize = False\
android.entrypoint = org.kivy.android.PythonActivity\
android.accept_sdk_license = True\
\
# Optymalizacje dla Galaxy A35 5G\
android.gradle_dependencies = androidx.work:work-runtime:2.7.1\
android.add_jars = androidx.work:work-runtime:2.7.1' buildozer.spec
fi

echo "Optymalizacja zakończona!"
echo "Utworzono kopię zapasową oryginalnego pliku jako 'buildozer.spec.backup'"
echo ""
echo "Aby zbudować aplikację, uruchom:"
echo "buildozer -v android debug"