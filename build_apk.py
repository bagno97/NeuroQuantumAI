#!/usr/bin/env python3
"""
Skrypt pomocniczy do budowania aplikacji Android APK
"""
import os
import shutil
import subprocess
import sys
from pathlib import Path

def check_requirements():
    """Sprawdza czy wszystkie wymagane narzędzia są dostępne"""
    print("Sprawdzam wymagane narzędzia...")
    
    try:
        # Sprawdzamy Buildozer
        subprocess.run(["buildozer", "--version"], check=True, capture_output=True)
        print("✓ Buildozer jest zainstalowany")
    except Exception:
        print("✗ Buildozer nie jest zainstalowany lub nie działa poprawnie")
        return False
    
    return True

def prepare_environment():
    """Przygotowuje środowisko do budowania dla Samsung Galaxy A35 5G"""
    print("Przygotowuję środowisko dla Samsung Galaxy A35 5G...")
    
    # Upewnij się, że buildozer.spec jest poprawny
    with open("buildozer.spec", "r") as f:
        spec = f.read()
    
    # Aktualizacja dla Samsung Galaxy A35 5G
    updates = {
        "android.minapi = 21": "android.minapi = 26",
        "android.sdk = 33": "android.sdk = 34",
        "android.archs = armeabi-v7a, arm64-v8a": "android.archs = arm64-v8a",
        "requirements = python3,": "requirements = python3==3.9.17,hostpython3==3.9.17,kivy==2.2.1,requests,plyer,pillow,urllib3,certifi,"
    }
    
    updated = False
    for old, new in updates.items():
        if old in spec:
            spec = spec.replace(old, new)
            updated = True
    
    # Dodaj konfigurację dla Galaxy A35 5G, jeśli nie istnieje
    if "[app.android]" in spec and "android.gradle_dependencies" not in spec:
        spec = spec.replace(
            "[app.android]",
            "[app.android]\n\n# Konfiguracja pod Samsung Galaxy A35 5G\n"
            "android.allow_backup = True\n"
            "android.presplash_color = #ffffff\n"
            "android.presplash.resize = False\n"
            "android.entrypoint = org.kivy.android.PythonActivity\n"
            "android.accept_sdk_license = True\n\n"
            "# Optymalizacje dla Galaxy A35 5G\n"
            "android.gradle_dependencies = androidx.work:work-runtime:2.7.1\n"
            "android.add_jars = androidx.work:work-runtime:2.7.1"
        )
        updated = True
    
    if updated:
        print("Aktualizuję buildozer.spec z konfiguracją dla Samsung Galaxy A35 5G...")
        with open("buildozer.spec", "w") as f:
            f.write(spec)
    
    print("✓ Środowisko przygotowane dla Samsung Galaxy A35 5G")
    return True

def build_debug_apk():
    """Buduje aplikację w trybie debug"""
    print("\nBuduję aplikację APK w trybie debug...")
    
    try:
        # Uruchamiamy buildozer z pełnym logowaniem
        process = subprocess.Popen(
            ["buildozer", "-v", "android", "debug"],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )
        
        # Czytamy wyjście w czasie rzeczywistym
        for line in process.stdout:
            print(line, end='')
        
        process.wait()
        
        if process.returncode != 0:
            print("\n✗ Budowanie APK nie powiodło się")
            return False
        
        print("\n✓ Budowanie APK zakończone sukcesem")
        return True
    
    except Exception as e:
        print(f"\n✗ Błąd podczas budowania APK: {e}")
        return False

def locate_apk():
    """Znajduje zbudowany plik APK"""
    print("\nLokalizuję zbudowany plik APK...")
    
    apk_dir = Path("./bin")
    if not apk_dir.exists():
        print("✗ Katalog bin nie istnieje - budowanie nie powiodło się")
        return None
    
    apk_files = list(apk_dir.glob("*.apk"))
    if not apk_files:
        print("✗ Nie znaleziono plików APK w katalogu bin")
        return None
    
    # Sortujemy po czasie modyfikacji - najnowszy na górze
    apk_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    newest_apk = apk_files[0]
    
    print(f"✓ Znaleziono APK: {newest_apk}")
    return newest_apk

def main():
    """Główna funkcja"""
    print("=== Narzędzie do budowania aplikacji Android NeuroQuantumAI ===\n")
    
    if not check_requirements():
        print("\nProszę zainstalować wymagane narzędzia i spróbować ponownie.")
        return 1
    
    if not prepare_environment():
        print("\nNie udało się przygotować środowiska.")
        return 1
    
    if not build_debug_apk():
        print("\nBudowanie APK nie powiodło się. Sprawdź logi, aby uzyskać więcej informacji.")
        return 1
    
    apk_path = locate_apk()
    if not apk_path:
        print("\nNie udało się znaleźć zbudowanego pliku APK.")
        return 1
    
    print(f"\nSukces! Plik APK został zbudowany: {apk_path}")
    print("\nAby zainstalować na Samsung Galaxy A35 5G:")
    print(f"1. Pobierz plik APK: {apk_path}")
    print("2. Przekaż go na urządzenie Samsung Galaxy A35 5G (przez USB, email lub chmurę)")
    print("3. Przejdź do Ustawienia > Biometria i zabezpieczenia > Zainstaluj nieznane aplikacje")
    print("4. Wybierz aplikację, którą użyjesz do instalacji (np. Menedżer plików)")
    print("5. Włącz przełącznik 'Zezwalaj z tego źródła'")
    print("6. Otwórz plik APK i postępuj zgodnie z instrukcjami instalacji")
    print("\nPamiętaj, że Samsung Galaxy A35 5G ma zabezpieczenia Knox, które mogą wymagać dodatkowych uprawnień.")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())