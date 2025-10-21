#!/usr/bin/env python3
"""
FULL_BUILD_ANDROID.py
=====================
KOMPLETNY SYSTEM BUILDOWANIA NEUROQUANTUMAI NA ANDROIDA
Stworzony z pełną wiedzą o projekcie - 100% funkcjonalności

ARCHITEKTURA PROJEKTU (przeanalizowano wszystkie pliki):
========================================================

1. GŁÓWNE PLIKI STARTOWE:
   - main.py: Standardowy start z Kivy
   - main_android_fixed.py: Android-optimized z lifecycle handling
   - main_full.py: Pełna wersja z wszystkimi funkcjami
   - main_simple.py: Wersja testowa

2. SILNIK AI (CORE):
   - AIEngine.py: Główny silnik AI z pełną funkcjonalnością
   - AIEngine_android.py: Android-safe version z safe_import()
   - ai_knowledge_base_universal.py: OGROMNA baza wiedzy + quantum search

3. FUNKCJE TELEFONU (PHONE):
   - phone_interface.py: PEŁNY dostęp do telefonu - kamera, GPS, SMS, połączenia, sensory
   - phone_permissions.json: Zarządzanie uprawnieniami AI
   - phone_activity.json: Log aktywności telefonu

4. SAMOMODYFIKACJA (SELF-EDIT):
   - self_editor.py: PEŁNA samomodyfikacja kodu - create, modify, delete, analyze
   - self_updater.py: System aktualizacji i rozwoju
   - editor_log.json: Log modyfikacji

5. PAMIĘĆ I EMOCJE:
   - memory_manager.py: Zarządzanie pamięcią długoterminową
   - emotion_memory.py: Analiza emocji
   - ai_memory.txt, long_memory.txt, emotion_memory.txt

6. SIECI NEURONOWE:
   - neuro_growth.py: Wzrost sieci neuronowych
   - network_generator.py: Generowanie nowych węzłów
   - synapse_manager.py: Zarządzanie synapsami
   - network_map.json, connections.json

7. ROZWÓJ I ROZSZERZENIA:
   - dynamic_loader.py: Dynamiczne ładowanie modułów
   - ai_extensions.py: System rozszerzeń
   - expansion.py: Rozbudowa logiki
   - neuro_architect.py: Architektura neuronowa

8. ZADANIA I INTERAKCJE:
   - task_executor.py: Wykonywanie zadań w tle
   - background_tasks.py: Zadania background
   - reinforcement_tracker.py: Uczenie wzmocnione
   - fact_checker.py: Sprawdzanie faktów

9. INTERFEJS UŻYTKOWNIKA:
   - neuroquantumai.kv: Główny interfejs Kivy
   - chat_gui.kv: Alternatywny interfejs czatu
   - icon.png: Ikona aplikacji

10. KONFIGURACJA:
    - requirements.txt: Zależności Python
    - buildozer.spec: Konfiguracja buildozer
    - AndroidManifest_addition.xml: Dodatkowe uprawnienia Android

WSZYSTKIE 16 UPRAWNIEŃ ANDROID:
- INTERNET, CAMERA, ACCESS_FINE_LOCATION, ACCESS_COARSE_LOCATION
- RECORD_AUDIO, READ/WRITE_EXTERNAL_STORAGE, READ/WRITE_CONTACTS
- SEND_SMS, RECEIVE_SMS, READ_SMS, CALL_PHONE, READ_CALL_LOG
- WRITE_CALL_LOG, READ_PHONE_STATE, MODIFY_AUDIO_SETTINGS
+ dodatkowe: ACCESS_NETWORK_STATE, ACCESS_WIFI_STATE, CHANGE_WIFI_STATE
+ BLUETOOTH, BLUETOOTH_ADMIN, VIBRATE, WAKE_LOCK, SYSTEM_ALERT_WINDOW
"""

import subprocess
import os
import sys
import shutil
import json
from pathlib import Path
from datetime import datetime

class NeuroQuantumAIBuilder:
    """
    Kompletny builder dla NeuroQuantumAI - zbuduje prawdziwą, działającą aplikację
    """
    
    def __init__(self):
        self.project_root = Path.cwd()
        self.build_log = []
        self.start_time = datetime.now()
        
        # WSZYSTKIE pliki projektu (przeanalizowane)
        self.python_files = [
            "main_android_fixed.py",  # GŁÓWNY plik startowy dla Android
            "AIEngine_android.py", "ai_knowledge_base_universal.py",
            "phone_interface.py", "self_editor.py", "self_updater.py",
            "memory_manager.py", "emotion_memory.py",
            "neuro_growth.py", "synapse_manager.py", "network_generator.py",
            "personality_core.py", "reinforcement_tracker.py",
            "dynamic_loader.py", "ai_extensions.py", "expansion.py",
            "task_executor.py", "background_tasks.py", "fact_checker.py",
            "system_requirements.py", "controller.py",
            "network_one.py", "network_zero.py", "neuro_architect.py",
            "ai_shell.py", "ai_web_shell.py", "chat_web.py",
            "google_drive_integration.py"
        ]
        
        self.data_files = [
            "neuroquantumai.kv", "chat_gui.kv", "icon.png",
            "ai_memory.txt", "long_memory.txt", "emotion_memory.txt",
            "network_map.json", "connections.json", "knowledge_map.json",
            "conversation_history.json", "editor_log.json",
            "phone_permissions.json", "phone_activity.json",
            "mrmory.json", "reinforcement.Json", "evolution_log.txt"
        ]
        
        # Pełne zależności (z requirements.txt + specyficzne dla Android)
        self.requirements = [
            "python3==3.9.17",
            "hostpython3==3.9.17", 
            "kivy==2.1.0",
            "setuptools",
            "requests",
            "plyer",
            "pillow==8.4.0",
            "pyjnius",
            "android",
            "sqlite3",
            "openssl",
            "libffi"
        ]
        
        self.log("🚀 NeuroQuantumAI Builder zainicjalizowany")
        self.log(f"📁 Projekt: {self.project_root}")
        self.log(f"📊 Plików Python: {len(self.python_files)}")
        self.log(f"📊 Plików danych: {len(self.data_files)}")
        
    def log(self, message: str):
        """Loguje wiadomość z timestampem"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        log_entry = f"[{timestamp}] {message}"
        print(log_entry)
        self.build_log.append(log_entry)
        
    def check_environment(self):
        """Sprawdza środowisko buildowania"""
        self.log("🔍 Sprawdzanie środowiska...")
        
        checks = {
            "Python": ["python3", "--version"],
            "Buildozer": ["buildozer", "--version"],
            "Git": ["git", "--version"]
        }
        
        for name, cmd in checks.items():
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
                version = result.stdout.strip() or result.stderr.strip()
                self.log(f"✅ {name}: {version}")
            except Exception as e:
                self.log(f"❌ {name}: BRAK - {e}")
                if name == "Buildozer":
                    self.log("📦 Instaluję Buildozer...")
                    subprocess.run([sys.executable, "-m", "pip", "install", "buildozer==1.5.0"])
                    
    def prepare_build_directory(self):
        """Przygotowuje katalogi buildowania"""
        self.log("📁 Przygotowuję katalogi...")
        
        # Usuń stare buildy
        dirs_to_clean = [".buildozer", "bin"]
        for dir_name in dirs_to_clean:
            dir_path = self.project_root / dir_name
            if dir_path.exists():
                self.log(f"🗑️  Usuwam {dir_name}/")
                shutil.rmtree(dir_path)
        
        # Utwórz bin/
        (self.project_root / "bin").mkdir(exist_ok=True)
        self.log("✅ Katalogi gotowe")
        
    def create_buildozer_spec(self):
        """Tworzy KOMPLETNY buildozer.spec z pełną wiedzą o projekcie"""
        self.log("📝 Tworzę nowy buildozer.spec...")
        
        spec_content = f'''[app]
# NeuroQuantumAI - Pełna konfiguracja buildozer
# Utworzono: {datetime.now().isoformat()}
# Wszystkie pliki i funkcje zachowane

title = NeuroQuantumAI
package.name = neuroquantumai
package.domain = com.neuroquantum

# Wersja
version = 1.0

# Źródła - WSZYSTKIE pliki!
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt,md,Json,log
source.include_patterns = assets/*,images/*.png
source.exclude_exts = spec,sh,pyc,pyo
source.exclude_dirs = tests,bin,.buildozer,venv,.venv,.git,.github
source.exclude_patterns = license,images/*/*.jpg

# Główny plik startowy - Android-optimized
source.main = main_android_fixed.py

# Wymagania - PEŁNA LISTA
requirements = {",".join(self.requirements)}

# Ikona
icon.filename = %(source.dir)s/icon.png

# Orientacja
orientation = portrait

# Android specyficzne
android.minapi = 26
android.api = 34
android.sdk = 34
android.ndk = 25b
android.archs = arm64-v8a

# PEŁNE UPRAWNIENIA - AI ma dostęp do wszystkiego!
android.permissions = INTERNET,CAMERA,ACCESS_FINE_LOCATION,ACCESS_COARSE_LOCATION,RECORD_AUDIO,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,READ_CONTACTS,WRITE_CONTACTS,SEND_SMS,RECEIVE_SMS,READ_SMS,CALL_PHONE,READ_CALL_LOG,WRITE_CALL_LOG,READ_PHONE_STATE,MODIFY_AUDIO_SETTINGS,ACCESS_NETWORK_STATE,ACCESS_WIFI_STATE,CHANGE_WIFI_STATE,BLUETOOTH,BLUETOOTH_ADMIN,VIBRATE,WAKE_LOCK,SYSTEM_ALERT_WINDOW,ACCESS_NOTIFICATION_POLICY,FOREGROUND_SERVICE,READ_PHONE_NUMBERS,ANSWER_PHONE_CALLS,REQUEST_INSTALL_PACKAGES

# Android manifest settings
android.manifest.intent_filters = 

# Services
services = 

# Bootstrap
p4a.bootstrap = sdl2

# Branch
p4a.branch = master

# Hook
p4a.hook = 

# Source URL
p4a.source_url = 

# Local recipes
p4a.local_recipes = 

# Port
p4a.port = 

# Whitelist
android.whitelist = lib-dynload/_csv.so

# Gradle dependencies
android.gradle_dependencies = androidx.work:work-runtime:2.7.1

# Android AAR
android.add_aars = 

# Android JARs
android.add_jars = 

# Android Java src
android.add_src = 

# Presplash
presplash.filename = %(source.dir)s/icon.png
presplash.color = #FFFFFF

# Full screen
fullscreen = 0

# Config files
android.add_compile_options = 
android.add_gradle_repositories = 
android.add_packaging_options = 

[buildozer]
log_level = 2
warn_on_root = 1
'''
        
        spec_path = self.project_root / "buildozer.spec"
        with open(spec_path, 'w', encoding='utf-8') as f:
            f.write(spec_content)
            
        self.log("✅ buildozer.spec utworzony")
        return spec_path
        
    def verify_all_files(self):
        """Weryfikuje czy wszystkie pliki projektu istnieją"""
        self.log("🔍 Weryfikuję pliki projektu...")
        
        missing = []
        for file_name in self.python_files + self.data_files:
            file_path = self.project_root / file_name
            if not file_path.exists():
                missing.append(file_name)
                self.log(f"⚠️  Brak: {file_name}")
            else:
                size = file_path.stat().st_size
                self.log(f"✅ {file_name} ({size} bytes)")
                
        if missing:
            self.log(f"❌ Brakuje {len(missing)} plików!")
            return False
        else:
            self.log(f"✅ Wszystkie {len(self.python_files + self.data_files)} plików dostępnych")
            return True
            
    def build_apk(self, debug=True):
        """Buduje APK używając buildozer"""
        self.log("🔨 Rozpoczynam budowanie APK...")
        
        build_type = "debug" if debug else "release"
        cmd = ["buildozer", "-v", "android", build_type]
        
        self.log(f"📟 Komenda: {' '.join(cmd)}")
        self.log("⏳ To może potrwać 30-60 minut...")
        self.log("☕ Czas na kawę! Buildozer robi całą robotę...")
        
        try:
            # Uruchom buildozer z pełnym logowaniem
            process = subprocess.Popen(
                cmd,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1
            )
            
            # Loguj output w czasie rzeczywistym
            for line in process.stdout:
                line = line.strip()
                if line:
                    print(f"    {line}")
                    self.build_log.append(line)
                    
            process.wait()
            
            if process.returncode == 0:
                self.log("✅ Buildowanie zakończone sukcesem!")
                return True
            else:
                self.log(f"❌ Buildowanie nie powiodło się (kod: {process.returncode})")
                return False
                
        except Exception as e:
            self.log(f"❌ Błąd podczas buildowania: {e}")
            return False
            
    def find_built_apk(self):
        """Znajduje zbudowany APK"""
        bin_dir = self.project_root / "bin"
        if not bin_dir.exists():
            return None
            
        apk_files = list(bin_dir.glob("*.apk"))
        if apk_files:
            return apk_files[0]
        return None
        
    def save_build_log(self):
        """Zapisuje log buildowania"""
        log_path = self.project_root / "FULL_BUILD_LOG.txt"
        with open(log_path, 'w', encoding='utf-8') as f:
            f.write(f"NeuroQuantumAI - Pełny log buildowania\n")
            f.write(f"{'='*70}\n")
            f.write(f"Start: {self.start_time.isoformat()}\n")
            f.write(f"Koniec: {datetime.now().isoformat()}\n")
            f.write(f"Czas trwania: {datetime.now() - self.start_time}\n")
            f.write(f"{'='*70}\n\n")
            f.write("\n".join(self.build_log))
        self.log(f"📄 Log zapisany: {log_path}")
        
    def run_full_build(self):
        """Uruchamia pełny proces buildowania"""
        self.log("\n" + "="*70)
        self.log("🚀 NEUROQUANTUMAI - PEŁNE BUILDOWANIE ANDROID")
        self.log("="*70 + "\n")
        
        # Krok 1: Sprawdź środowisko
        self.check_environment()
        
        # Krok 2: Przygotuj katalogi
        self.prepare_build_directory()
        
        # Krok 3: Weryfikuj pliki
        if not self.verify_all_files():
            self.log("❌ Nie można kontynuować - brakuje plików!")
            return False
            
        # Krok 4: Stwórz buildozer.spec
        self.create_buildozer_spec()
        
        # Krok 5: Buduj APK
        success = self.build_apk(debug=True)
        
        # Krok 6: Znajdź APK
        if success:
            apk = self.find_built_apk()
            if apk:
                size_mb = apk.stat().st_size / (1024 * 1024)
                self.log(f"\n🎉 SUKCES! APK zbudowany:")
                self.log(f"📦 Plik: {apk}")
                self.log(f"📊 Rozmiar: {size_mb:.2f} MB")
                self.log(f"⏱️  Czas: {datetime.now() - self.start_time}")
            else:
                self.log("⚠️  Buildowanie zakończone, ale nie znaleziono APK")
                success = False
        
        # Krok 7: Zapisz log
        self.save_build_log()
        
        self.log("\n" + "="*70)
        if success:
            self.log("✅ BUILDOWANIE ZAKOŃCZONE SUKCESEM!")
        else:
            self.log("❌ BUILDOWANIE NIE POWIODŁO SIĘ")
        self.log("="*70)
        
        return success

if __name__ == "__main__":
    print("🤖 NeuroQuantumAI - Full Android Builder")
    print("=" * 70)
    print("Ten builder został stworzony z pełną wiedzą o projekcie:")
    print("- 27 plików Python (wszystkie moduły AI)")
    print("- 16 plików danych (bazy wiedzy, pamięć, konfiguracja)")
    print("- Pełne uprawnienia Android (telefon, sensory, storage)")
    print("- Kompletna funkcjonalność AI (pamięć, emocje, samomodyfikacja)")
    print("=" * 70)
    print()
    
    response = input("Rozpocząć pełne buildowanie? (t/n): ").lower().strip()
    
    if response in ['t', 'tak', 'yes', 'y']:
        builder = NeuroQuantumAIBuilder()
        builder.run_full_build()
    else:
        print("❌ Buildowanie anulowane")
