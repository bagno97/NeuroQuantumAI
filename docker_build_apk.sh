#!/bin/bash
# docker_build_apk.sh - Skrypt do budowy APK przy użyciu kontenera Docker
# Dostosowany dla Samsung Galaxy A35 5G

set -e

echo "=== Budowanie APK dla Samsung Galaxy A35 5G przy użyciu Docker ==="

# Sprawdź czy Docker jest dostępny
if ! command -v docker &> /dev/null; then
    echo "Docker nie jest zainstalowany. Instaluję..."
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl gnupg lsb-release
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io
fi

# Upewnij się, że buildozer.spec jest dostosowany do Samsung Galaxy A35 5G
echo "Dostosowuję konfigurację do Samsung Galaxy A35 5G..."

# Funkcja do edycji pliku buildozer.spec
update_buildozer_spec() {
    local file="buildozer.spec"
    # Ustawienie minimalnej wersji API i SDK
    sed -i 's/android.minapi = .*/android.minapi = 26/' $file
    sed -i 's/android.sdk = .*/android.sdk = 34/' $file
    # Ustawienie tylko dla architektury arm64-v8a (Samsung Galaxy A35 5G)
    sed -i 's/android.archs = .*/android.archs = arm64-v8a/' $file
    # Upewnij się, że ikona jest poprawnie ustawiona
    if ! grep -q "icon.filename" $file; then
        sed -i 's/# icon.filename = .*/icon.filename = %(source.dir)s\/icon.png/' $file
    fi
    # Zaktualizuj zależności
    if grep -q "requirements = python3," $file; then
        sed -i 's/requirements = python3,/requirements = python3==3.9.17,hostpython3==3.9.17,kivy==2.2.1,requests,plyer,pillow,urllib3,certifi,/' $file
    fi
    
    # Dodaj sekcję app.android jeśli nie istnieje
    if ! grep -q "\[app.android\]" $file; then
        echo "" >> $file
        echo "[app.android]" >> $file
        echo "" >> $file
    fi
    
    # Dodaj optymalizacje dla Samsung Galaxy A35 5G
    if ! grep -q "android.allow_backup" $file; then
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
android.add_jars = androidx.work:work-runtime:2.7.1' $file
    fi
}

# Wykonaj aktualizację specyfikacji buildozer
update_buildozer_spec

echo "Konfiguracja zaktualizowana."

# Uruchom kontener Docker z oficjalnym obrazem kivy/buildozer
echo "Uruchamiam budowanie w kontenerze Docker..."

# Tworzymy własny skrypt, który wykona wszystkie czynności wewnątrz kontenera
cat > /tmp/container_build.sh << 'EOF'
#!/bin/bash
cd /app
# Zapobiegamy pytaniu o root user
export USE_UNSUPPORTED_PYTHON_VERSION=1
echo "y" | buildozer -v android debug
EOF

chmod +x /tmp/container_build.sh

# Uruchamiamy kontener Docker z innym obrazem, który zawiera już Android SDK
echo "Pobieranie obrazu Docker baterflyrity/buildozer i uruchamianie procesu budowania..."
docker run --rm -v "$(pwd)":/app -w /app baterflyrity/buildozer buildozer -v android debug

# Sprawdź czy APK zostało wygenerowane
if [ -f "bin/neuroquantumai-0.2-debug.apk" ]; then
    echo "=== SUKCES! ==="
    echo "APK zostało zbudowane pomyślnie dla Samsung Galaxy A35 5G."
    echo "Plik APK znajduje się w: bin/neuroquantumai-0.2-debug.apk"
    echo ""
    echo "Aby zainstalować na Samsung Galaxy A35 5G:"
    echo "1. Przekaż plik APK na urządzenie (przez USB, email lub chmurę)"
    echo "2. Przejdź do Ustawienia > Biometria i zabezpieczenia > Zainstaluj nieznane aplikacje"
    echo "3. Wybierz aplikację, którą użyjesz do instalacji (np. Menedżer plików)"
    echo "4. Włącz przełącznik 'Zezwalaj z tego źródła'"
    echo "5. Otwórz plik APK i zainstaluj aplikację"
    echo ""
    echo "Pamiętaj, że Samsung Galaxy A35 5G ma zabezpieczenia Knox, które mogą wymagać dodatkowych uprawnień."
else
    echo "=== BŁĄD! ==="
    echo "Coś poszło nie tak podczas budowania APK."
    echo "Sprawdź logi buildozera w katalogu .buildozer/"
fi