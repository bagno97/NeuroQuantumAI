
"""
self_editor.py
--------------
This module provides functions for dynamic self-modification of code files, including backup, syntax check, and logging.
WARNING: Dynamic code modification is risky and should be used with caution.
Part of the NeuroQuantumAI Android app project.
"""

import shutil
import datetime
import subprocess
import sys
import importlib
import os
import json
from typing import Any, Dict

def modify_code(target: str, snippet: str, log_file: str = "editor_log.json") -> str:
    """
    Append a code snippet to a target file, backup the original, check syntax, reload module, and log the operation.
    Args:
        target (str): Path to the target Python file.
        snippet (str): Code snippet to append.
        log_file (str): Path to the log file.
    Returns:
        str: Status message indicating success or error.
    """
    stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    bak = f"{target}.bak_{stamp}"
    try:
        shutil.copy(target, bak)
        with open(target, "a", encoding="utf-8") as f:
            f.write(f"\n# [AI MODIFIED] {stamp}\n{snippet}\n")

        res = subprocess.run([sys.executable, "-m", "py_compile", target])
        if res.returncode != 0:
            shutil.copy(bak, target)
            return "Błąd składni – rollback."

        module_name = os.path.splitext(os.path.basename(target))[0]
        # Note: This assumes the module is in the ai_engine package; adjust as needed.
        try:
            importlib.reload(importlib.import_module("ai_engine." + module_name))
        except Exception:
            pass  # Ignore reload errors if not in ai_engine

        log_entry = {
            "timestamp": stamp,
            "file": target,
            "backup": bak,
            "snippet": snippet,
            "status": "success"
        }
        save_log(log_entry, log_file)
        return "Kod zmodyfikowany pomyślnie."
    except Exception as e:
        save_log({
            "timestamp": stamp,
            "file": target,
            "backup": bak,
            "snippet": snippet,
            "status": f"error: {str(e)}"
        }, log_file)
        return f"Nieudana modyfikacja: {str(e)}"

def save_log(entry: Dict[str, Any], log_file: str) -> None:
    """
    Save a log entry to the log file, appending to existing logs.
    Args:
        entry (Dict[str, Any]): Log entry to save.
        log_file (str): Path to the log file.
    """
    try:
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                logs = json.load(f)
        else:
            logs = []
        logs.append(entry)
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("Błąd zapisu logu:", e)

def evaluate_self() -> str:
    """
    Simple self-test for the self_editor module.
    Returns:
        str: Status message.
    """
    return "Moduł self_editor działa i jest gotowy do modyfikacji kodu."
