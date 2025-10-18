#!/bin/bash
# build_apk_direct.sh - Skrypt do bezpośredniego budowania APK dla Samsung Galaxy A35 5G
set -e

echo "=== Przygotowuję bezpośrednie budowanie APK dla Samsung Galaxy A35 5G ==="

# Utwórz plik APK w formacie ZIP (jako prototyp)
echo "Tworzę prototypowy plik APK (ZIP)..."

# Utwórz tymczasowy katalog do przygotowania plików
mkdir -p /tmp/android_app/bin
mkdir -p /tmp/android_app/assets

# Przygotuj podstawowe pliki potrzebne do APK
echo "Kopiuję pliki projektu do tymczasowego katalogu..."
cp -r *.py /tmp/android_app/assets/
cp -r *.kv /tmp/android_app/assets/ 2>/dev/null || echo "Brak plików .kv"
cp -r *.json /tmp/android_app/assets/ 2>/dev/null || echo "Brak plików .json"
cp -r *.txt /tmp/android_app/assets/ 2>/dev/null || echo "Brak plików .txt"
cp icon.png /tmp/android_app/assets/ 2>/dev/null || echo "Brak pliku icon.png"

# Utwórz plik AndroidManifest.xml z odpowiednimi uprawnieniami dla Samsung Galaxy A35 5G
cat > /tmp/android_app/AndroidManifest.xml << 'EOF'
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.neuroquantumai"
    android:versionCode="1"
    android:versionName="0.2">

    <uses-sdk android:minSdkVersion="26" android:targetSdkVersion="34" />
    
    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.CAMERA" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />

    <application
        android:label="NeuroQuantumAI"
        android:icon="@drawable/icon"
        android:allowBackup="true"
        android:theme="@android:style/Theme.NoTitleBar">
        <activity
            android:name="org.kivy.android.PythonActivity"
            android:configChanges="orientation|keyboardHidden|screenSize"
            android:screenOrientation="portrait"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
    </application>
</manifest>
EOF

# Utwórz plik README.txt z instrukcjami dla użytkownika
cat > /tmp/android_app/README.txt << 'EOF'
NeuroQuantumAI - Prototypowy plik APK

Ten plik zawiera prototypową wersję aplikacji NeuroQuantumAI zoptymalizowaną dla Samsung Galaxy A35 5G.
Ze względu na ograniczenia środowiska Codespace, ten plik nie jest prawdziwym plikiem APK, 
ale zawiera wszystkie potrzebne pliki do budowy APK na lokalnym komputerze.

Instrukcje budowania APK:
1. Rozpakuj zawartość tego pliku ZIP
2. Zainstaluj Buildozer według instrukcji z pliku BUILD_INSTRUCTIONS.md
3. Uruchom skrypt build_android.sh lub build_apk.py

W przypadku problemów skontaktuj się z autorem aplikacji.
EOF

# Stwórz plik budowania dla Samsung Galaxy A35
cat > /tmp/android_app/BUILD_FOR_SAMSUNG_A35.sh << 'EOF'
#!/bin/bash
# Skrypt do budowy APK dla Samsung Galaxy A35 5G

echo "Rozpoczynam budowanie APK dla Samsung Galaxy A35 5G..."
echo "Wymagania: Python 3.9+, Buildozer, Java JDK 11"

pip install buildozer==1.5.0 cython==0.29.33

# Utwórz plik buildozer.spec
cat > buildozer.spec << 'END'
[app]
title = NeuroQuantumAI
package.name = neuroquantumai
package.domain = com.example
source.dir = assets
source.include_exts = py,png,jpg,kv,atlas,json,txt
icon.filename = %(source.dir)s/icon.png
version = 0.2
requirements = python3==3.9.17,hostpython3==3.9.17,kivy==2.2.1,requests,plyer,pillow,urllib3,certifi
orientation = portrait
android.minapi = 26
android.api = 34
android.sdk = 34
android.ndk = 25b
android.archs = arm64-v8a
android.permissions = INTERNET, CAMERA, ACCESS_FINE_LOCATION, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
color = always
verbose = 2

[app.android]
android.allow_backup = True
android.presplash_color = #ffffff
android.presplash.resize = False
android.entrypoint = org.kivy.android.PythonActivity
android.accept_sdk_license = True
android.gradle_dependencies = androidx.work:work-runtime:2.7.1
android.add_jars = androidx.work:work-runtime:2.7.1
END

echo "Uruchamiam budowanie APK..."
buildozer -v android debug

if [ -f "bin/neuroquantumai-0.2-debug.apk" ]; then
    echo "Budowanie zakończone sukcesem!"
    echo "Plik APK znajduje się w katalogu bin/"
else
    echo "Wystąpił błąd podczas budowania APK."
fi
EOF

chmod +x /tmp/android_app/BUILD_FOR_SAMSUNG_A35.sh

# Skopiuj ważne pliki instrukcji
cp BUILD_INSTRUCTIONS.md /tmp/android_app/
cp SAMSUNG_A35_BUILD_NOTES.md /tmp/android_app/

# Spakuj wszystko do ZIP (prototypowy APK)
echo "Tworzę plik ZIP z przygotowanymi materiałami..."
cd /tmp/android_app
zip -r neuroquantumai-prototype.zip ./*

# Przenieś plik do katalogu bin projektu
mkdir -p /workspaces/NeuroQuantumAI/bin
cp neuroquantumai-prototype.zip /workspaces/NeuroQuantumAI/bin/neuroquantumai-samsung-a35-prototype.zip

echo "=== GOTOWE! ==="
echo "Prototypowy plik APK został utworzony: bin/neuroquantumai-samsung-a35-prototype.zip"
echo ""
echo "Ten plik zawiera wszystkie niezbędne materiały do zbudowania APK na lokalnym komputerze."
echo "Rozpakuj go i użyj dołączonego skryptu BUILD_FOR_SAMSUNG_A35.sh, aby zbudować pełny APK."
echo ""
echo "Aby zainstalować na Samsung Galaxy A35 5G:"
echo "1. Zbuduj APK zgodnie z instrukcjami w pliku"
echo "2. Przenieś wygenerowany plik APK na urządzenie"
echo "3. Przejdź do Ustawienia > Biometria i zabezpieczenia > Zainstaluj nieznane aplikacje"
echo "4. Wybierz aplikację do instalacji i włącz przełącznik 'Zezwalaj z tego źródła'"
echo "5. Zainstaluj aplikację"