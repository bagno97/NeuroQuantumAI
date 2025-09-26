
"""
phone_interface.py
------------------
This module provides an interface for controlling phone features via Termux commands on Android.
WARNING: This code is intended for use in a Termux/Android environment and uses subprocess to call system commands.
"""

import subprocess
from typing import Optional

def use_phone_feature(ui: str) -> str:
    """
    Parse user input and trigger phone features (camera, location, call, SMS) via Termux commands.
    Args:
        ui (str): User input string describing the desired phone action.
    Returns:
        str: Status message or result of the action.
    """
    ui = ui.lower()
    try:
        if "zrób zdjęcie" in ui:
            subprocess.run(["termux-camera-photo", "photo.jpg"])
            return "Zrobiłem zdjęcie: photo.jpg"
        if "lokalizacja" in ui:
            loc = subprocess.check_output(["termux-location"])
            return f"Moja lokalizacja: {loc.decode().strip()}"
        if "zadzwoń do" in ui:
            num = ui.split("do")[-1].strip()
            subprocess.run(["termux-telephony-call", num])
            return f"Dzwonię do {num}"
        if "wyślij sms" in ui:
            parts = ui.split("treść")
            num = parts[0].split("do")[-1].strip()
            msg = parts[1].strip() if len(parts) > 1 else ""
            subprocess.run(["termux-sms-send", "-n", num, msg])
            return f"Wyślij sms do {num}: {msg}"
    except Exception as e:
        return f"Błąd podczas obsługi funkcji telefonu: {e}"
    return ""
