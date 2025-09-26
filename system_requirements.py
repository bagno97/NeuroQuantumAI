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

def environment_report() -> str:
    """
    Zwraca raport o możliwościach środowiska do samomodyfikacji AI.
    """
    report = []
    report.append(f"Filesystem access: {'OK' if check_filesystem_access() else 'BRAK'}")
    report.append(f"Python interpreter: {'OK' if check_python_interpreter() else 'BRAK'}")
    report.append(f"System tools (shutil, subprocess, os, sys): {'OK' if check_system_tools() else 'BRAK'}")
    report.append(f"Terminal access: {'OK' if check_terminal_access() else 'BRAK'}")
    return "\n".join(report)
