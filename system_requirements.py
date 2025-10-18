"""
system_requirements.py
---------------------
Ten moduł pozwala AI sprawdzić, czy środowisko spełnia wymagania do samomodyfikacji kodu.
Może być używany przez AIEngine do ostrzegania użytkownika lub automatycznego wykrywania możliwości.
"""

import os
import sys
import shutil
import subprocess

REQUIRED_MODULES = ["shutil", "subprocess", "os", "sys"]


def check_filesystem_access(path: str = ".") -> bool:
    """
    Sprawdza, czy AI ma prawo zapisu i odczytu w katalogu.
    """
    try:
        testfile = os.path.join(path, "__ai_testfile.txt")
        with open(testfile, "w") as f:
            f.write("test")
        with open(testfile, "r") as f:
            _ = f.read()
        os.remove(testfile)
        return True
    except Exception:
        return False

def check_python_interpreter() -> bool:
    """
    Sprawdza, czy interpreter Python jest dostępny i pozwala na kompilację kodu.
    """
    try:
        code = "print('AI test')"
        res = subprocess.run([sys.executable, "-c", code], capture_output=True, timeout=3)
        return res.returncode == 0 and b"AI test" in res.stdout
    except Exception:
        return False

def check_system_tools() -> bool:
    """
    Sprawdza, czy wymagane moduły systemowe są dostępne.
    """
    for mod in REQUIRED_MODULES:
        if mod not in sys.modules and not shutil.which(mod):
            return False
    return True

def check_terminal_access() -> bool:
    """
    Sprawdza, czy AI może uruchamiać polecenia powłoki.
    """
    try:
        res = subprocess.run(["echo", "AI terminal test"], capture_output=True, timeout=3)
        return res.returncode == 0 and b"AI terminal test" in res.stdout
    except Exception:
        return False

def find_writable_dirs() -> list:
    """
    Znajduje katalogi dostępne do zapisu w różnych środowiskach (Android, Linux, Windows).
    Zwraca listę ścieżek, które mogą być użyte do przechowywania dynamicznie tworzonych modułów.
    """
    writable_dirs = []
    
    # Sprawdź katalogi specyficzne dla Androida
    android_dirs = [
        "/data/data/org.test.neuroquantumai/files",  # Zmień na właściwą nazwę pakietu
        "/storage/emulated/0/Android/data/org.test.neuroquantumai/files",
        "/sdcard/Android/data/org.test.neuroquantumai/files"
    ]
    
    # Sprawdź katalogi na różnych systemach
    system_dirs = [
        ".",  # Bieżący katalog
        os.path.join(os.path.expanduser("~"), "NeuroQuantumAI_modules"),
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "dynamic_modules"),
        "/tmp/neuroquantumai"  # Dla systemów Unix/Linux
    ]
    
    # Sprawdź wszystkie możliwe katalogi
    all_dirs = android_dirs + system_dirs
    
    for directory in all_dirs:
        try:
            # Utwórz katalog, jeśli nie istnieje
            os.makedirs(directory, exist_ok=True)
            
            # Sprawdź, czy można w nim zapisywać
            if check_filesystem_access(directory):
                writable_dirs.append(directory)
        except Exception:
            pass
    
    return writable_dirs

def get_best_dynamic_dir() -> str:
    """
    Zwraca najlepszy katalog do przechowywania dynamicznie generowanych modułów.
    """
    dirs = find_writable_dirs()
    if dirs:
        return dirs[0]  # Pierwszy znaleziony katalog z dostępem do zapisu
    else:
        return "."  # Bieżący katalog jako ostateczność

def environment_report() -> str:
    """
    Zwraca raport o możliwościach środowiska do samomodyfikacji AI.
    """
    report = []
    report.append(f"Filesystem access: {'OK' if check_filesystem_access() else 'BRAK'}")
    report.append(f"Python interpreter: {'OK' if check_python_interpreter() else 'BRAK'}")
    report.append(f"System tools (shutil, subprocess, os, sys): {'OK' if check_system_tools() else 'BRAK'}")
    report.append(f"Terminal access: {'OK' if check_terminal_access() else 'BRAK'}")
    
    # Dodaj informacje o katalogach dostępnych do zapisu
    writable_dirs = find_writable_dirs()
    report.append(f"Writable directories: {len(writable_dirs)} found")
    for directory in writable_dirs:
        report.append(f"  - {directory}")
    
    return "\n".join(report)
