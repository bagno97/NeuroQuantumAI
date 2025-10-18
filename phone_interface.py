
"""
phone_interface.py
------------------
PEŁNY DOSTĘP DO TELEFONU - AI może korzystać z telefonu jak człowiek!
Obsługuje wszystkie funkcje telefonu przez Termux/Plyer/Native Android API.
Brak ograniczeń - AI ma pełną kontrolę nad urządzeniem z zgodą użytkownika.
"""

import subprocess
import os
import json
import time
from typing import Optional, Dict, List, Any
from datetime import datetime

# Ścieżka do pliku uprawnień i konfiguracji
PERMISSIONS_FILE = "phone_permissions.json"
PHONE_LOG = "phone_activity.json"

def load_permissions() -> Dict[str, bool]:
    """Ładuje ustawienia uprawnień AI do funkcji telefonu."""
    try:
        with open(PERMISSIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        # Domyślnie AI ma wszystkie uprawnienia (z możliwością wyłączenia przez użytkownika)
        default_perms = {
            "camera": True, "location": True, "sms": True, "calls": True,
            "contacts": True, "files": True, "notifications": True, 
            "bluetooth": True, "wifi": True, "microphone": True,
            "sensors": True, "battery": True, "system_info": True,
            "internet": True, "storage": True, "clipboard": True
        }
        save_permissions(default_perms)
        return default_perms

def save_permissions(perms: Dict[str, bool]):
    """Zapisuje ustawienia uprawnień."""
    with open(PERMISSIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(perms, f, ensure_ascii=False, indent=2)

def log_phone_activity(action: str, result: str, timestamp: str = None):
    """Loguje aktywność AI na telefonie."""
    if not timestamp:
        timestamp = datetime.now().isoformat()
    
    try:
        with open(PHONE_LOG, "r", encoding="utf-8") as f:
            log = json.load(f)
    except:
        log = []
    
    log.append({"timestamp": timestamp, "action": action, "result": result})
    
    # Zachowaj tylko ostatnie 1000 wpisów
    if len(log) > 1000:
        log = log[-1000:]
    
    with open(PHONE_LOG, "w", encoding="utf-8") as f:
        json.dump(log, f, ensure_ascii=False, indent=2)

def use_phone_feature(ui: str) -> str:
    """
    ROZSZERZONA OBSŁUGA TELEFONU - AI może korzystać z wszystkich funkcji!
    """
    ui = ui.lower().strip()
    permissions = load_permissions()
    
    try:
        # === KAMERA I MULTIMEDIA ===
        if any(word in ui for word in ["zrób zdjęcie", "foto", "camera", "kamera"]):
            if not permissions.get("camera", True):
                return "❌ Brak uprawnień do kamery. Użyj: 'pozwól ai kamera'"
            
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"ai_photo_{timestamp}.jpg"
            
            # Termux + Plyer fallback
            try:
                subprocess.run(["termux-camera-photo", filename], check=True)
                result = f"📸 Zrobiłem zdjęcie: {filename}"
            except:
                try:
                    from plyer import camera
                    camera.take_picture(filename=filename, on_complete=lambda x: None)
                    result = f"📸 Zrobiłem zdjęcie: {filename} (Plyer)"
                except:
                    result = "❌ Nie mogę uzyskać dostępu do kamery"
            
            log_phone_activity("camera_photo", result)
            return result

        # === LOKALIZACJA I GPS ===
        if any(word in ui for word in ["lokalizacja", "gps", "gdzie jestem", "location"]):
            if not permissions.get("location", True):
                return "❌ Brak uprawnień do lokalizacji. Użyj: 'pozwól ai lokalizacja'"
            
            try:
                # Termux location
                loc_output = subprocess.check_output(["termux-location", "-p", "gps"], timeout=10)
                loc_data = json.loads(loc_output.decode())
                lat, lon = loc_data.get("latitude", 0), loc_data.get("longitude", 0)
                result = f"📍 Lokalizacja: {lat:.6f}, {lon:.6f} (GPS)"
            except:
                try:
                    from plyer import gps
                    gps.configure(on_location=lambda **kwargs: kwargs)
                    gps.start()
                    time.sleep(2)
                    gps.stop()
                    result = "📍 Próbuję uzyskać lokalizację (Plyer)..."
                except:
                    result = "❌ Nie mogę uzyskać lokalizacji"
            
            log_phone_activity("location", result)
            return result

        # === TELEFON I SMS ===
        if "zadzwoń" in ui or "call" in ui:
            if not permissions.get("calls", True):
                return "❌ Brak uprawnień do połączeń. Użyj: 'pozwól ai połączenia'"
            
            # Wyciągnij numer telefonu
            number = extract_phone_number(ui)
            if not number:
                return "❌ Nie podałeś numeru telefonu"
            
            try:
                subprocess.run(["termux-telephony-call", number], check=True)
                result = f"📞 Dzwonię do {number}"
            except:
                result = f"❌ Nie mogę zadzwonić do {number}"
            
            log_phone_activity("phone_call", f"{result} ({number})")
            return result

        if "sms" in ui or "wiadomość" in ui:
            if not permissions.get("sms", True):
                return "❌ Brak uprawnień do SMS. Użyj: 'pozwól ai sms'"
            
            number, message = extract_sms_data(ui)
            if not number or not message:
                return "❌ Podaj numer i treść SMS: 'wyślij sms do 123456789 treść wiadomość'"
            
            try:
                subprocess.run(["termux-sms-send", "-n", number, message], check=True)
                result = f"💬 SMS wysłany do {number}: {message[:50]}..."
            except:
                result = f"❌ Nie mogę wysłać SMS do {number}"
            
            log_phone_activity("sms", f"{result}")
            return result

        # === KONTAKTY ===
        if "kontakty" in ui or "contacts" in ui:
            if not permissions.get("contacts", True):
                return "❌ Brak uprawnień do kontaktów"
            
            try:
                contacts = subprocess.check_output(["termux-contact-list"], timeout=5)
                result = f"📋 Kontakty: {contacts.decode()[:200]}..."
            except:
                result = "❌ Nie mogę pobrać kontaktów"
            
            log_phone_activity("contacts", "Pobrano listę kontaktów")
            return result

        # === PLIKI I STORAGE ===
        if any(word in ui for word in ["pliki", "files", "storage", "browse"]):
            if not permissions.get("files", True):
                return "❌ Brak uprawnień do plików"
            
            try:
                # Lista plików w storage
                files = subprocess.check_output(["ls", "/storage/emulated/0/"], timeout=5)
                result = f"📁 Pliki: {files.decode()[:200]}..."
            except:
                result = "❌ Nie mogę przeglądać plików"
            
            return result

        # === POWIADOMIENIA ===
        if "powiadomienie" in ui or "notification" in ui:
            if not permissions.get("notifications", True):
                return "❌ Brak uprawnień do powiadomień"
            
            title = "NeuroQuantumAI"
            message = ui.replace("powiadomienie", "").strip() or "Powiadomienie od AI"
            
            try:
                from plyer import notification
                notification.notify(title=title, message=message, timeout=5)
                result = f"🔔 Powiadomienie: {message}"
            except:
                try:
                    subprocess.run(["termux-notification", "--title", title, "--content", message])
                    result = f"🔔 Powiadomienie (Termux): {message}"
                except:
                    result = "❌ Nie mogę wysłać powiadomienia"
            
            log_phone_activity("notification", result)
            return result

        # === MIKROFON I NAGRYWANIE ===
        if any(word in ui for word in ["nagraj", "mikrofon", "record", "audio"]):
            if not permissions.get("microphone", True):
                return "❌ Brak uprawnień do mikrofonu"
            
            duration = extract_number_from_text(ui) or 5  # domyślnie 5 sekund
            filename = f"ai_recording_{datetime.now().strftime('%Y%m%d_%H%M%S')}.m4a"
            
            try:
                subprocess.run(["termux-microphone-record", "-f", filename, "-l", str(duration)], timeout=duration+5)
                result = f"🎤 Nagranie zapisane: {filename} ({duration}s)"
            except:
                result = "❌ Nie mogę nagrać dźwięku"
            
            log_phone_activity("microphone", result)
            return result

        # === BLUETOOTH ===
        if "bluetooth" in ui:
            if not permissions.get("bluetooth", True):
                return "❌ Brak uprawnień do Bluetooth"
            
            try:
                bt_info = subprocess.check_output(["termux-bluetooth-info"], timeout=5)
                result = f"📶 Bluetooth: {bt_info.decode()[:200]}..."
            except:
                result = "❌ Nie mogę sprawdzić Bluetooth"
            
            return result

        # === WIFI ===
        if "wifi" in ui:
            if not permissions.get("wifi", True):
                return "❌ Brak uprawnień do WiFi"
            
            try:
                wifi_info = subprocess.check_output(["termux-wifi-connectioninfo"], timeout=5)
                result = f"📶 WiFi: {wifi_info.decode()[:200]}..."
            except:
                result = "❌ Nie mogę sprawdzić WiFi"
            
            return result

        # === SENSORY ===
        if any(word in ui for word in ["sensors", "sensory", "accelerometer", "gyroscope"]):
            if not permissions.get("sensors", True):
                return "❌ Brak uprawnień do sensorów"
            
            try:
                sensor_data = subprocess.check_output(["termux-sensor", "-l"], timeout=5)
                result = f"📱 Sensory: {sensor_data.decode()[:200]}..."
            except:
                result = "❌ Nie mogę odczytać sensorów"
            
            return result

        # === BATERIA ===
        if "bateria" in ui or "battery" in ui:
            try:
                battery_info = subprocess.check_output(["termux-battery-status"], timeout=5)
                battery_data = json.loads(battery_info.decode())
                level = battery_data.get("percentage", "nieznany")
                status = battery_data.get("status", "nieznany")
                result = f"🔋 Bateria: {level}% ({status})"
            except:
                result = "❌ Nie mogę sprawdzić baterii"
            
            return result

        # === SCHOWEK ===
        if "schowek" in ui or "clipboard" in ui:
            if not permissions.get("clipboard", True):
                return "❌ Brak uprawnień do schowka"
            
            if "zapisz" in ui or "copy" in ui:
                text = ui.replace("schowek", "").replace("zapisz", "").strip()
                try:
                    subprocess.run(["termux-clipboard-set", text], check=True)
                    result = f"📋 Zapisano do schowka: {text[:50]}..."
                except:
                    result = "❌ Nie mogę zapisać do schowka"
            else:
                try:
                    clipboard_content = subprocess.check_output(["termux-clipboard-get"], timeout=5)
                    result = f"📋 Schowek: {clipboard_content.decode()[:200]}..."
                except:
                    result = "❌ Schowek jest pusty lub niedostępny"
            
            return result

        # === UPRAWNIENIA ===
        if "pozwól ai" in ui:
            return manage_permissions(ui)

        # === INNE FUNKCJE ===
        return "❓ Nie rozpoznaję tej komendy telefonu. Dostępne: zdjęcie, lokalizacja, sms, dzwoń, kontakty, pliki, powiadomienie, nagraj, bluetooth, wifi, sensory, bateria, schowek"

    except Exception as e:
        error_msg = f"❌ Błąd funkcji telefonu: {e}"
        log_phone_activity("error", error_msg)
        return error_msg

def extract_phone_number(text: str) -> Optional[str]:
    """Wyciąga numer telefonu z tekstu."""
    import re
    # Szuka wzorców numerów telefonu
    patterns = [
        r'\b\d{9}\b',           # 123456789
        r'\b\d{3}[-\s]?\d{3}[-\s]?\d{3}\b',  # 123-456-789
        r'\+\d{1,3}[-\s]?\d{7,12}\b'  # +48-123456789
    ]
    
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group().replace("-", "").replace(" ", "")
    return None

def extract_sms_data(text: str) -> tuple:
    """Wyciąga numer i treść SMS z tekstu."""
    try:
        # Format: "wyślij sms do 123456789 treść wiadomość"
        if " do " in text and " treść " in text:
            parts = text.split(" treść ")
            number_part = parts[0].split(" do ")[-1].strip()
            message = parts[1].strip()
            number = extract_phone_number(number_part)
            return number, message
    except:
        pass
    return None, None

def extract_number_from_text(text: str) -> Optional[int]:
    """Wyciąga liczbę z tekstu."""
    import re
    match = re.search(r'\b(\d+)\b', text)
    return int(match.group()) if match else None

def manage_permissions(ui: str) -> str:
    """Zarządzanie uprawnieniami AI."""
    perms = load_permissions()
    
    if "kamera" in ui:
        perms["camera"] = True
        save_permissions(perms)
        return "✅ AI ma teraz dostęp do kamery"
    elif "lokalizacja" in ui:
        perms["location"] = True
        save_permissions(perms)
        return "✅ AI ma teraz dostęp do lokalizacji"
    elif "sms" in ui:
        perms["sms"] = True
        save_permissions(perms)
        return "✅ AI ma teraz dostęp do SMS"
    elif "połączenia" in ui:
        perms["calls"] = True
        save_permissions(perms)
        return "✅ AI ma teraz dostęp do połączeń"
    elif "wszystko" in ui:
        for key in perms:
            perms[key] = True
        save_permissions(perms)
        return "✅ AI ma teraz pełny dostęp do telefonu!"
    
    return "❓ Użyj: 'pozwól ai wszystko' lub 'pozwól ai kamera/lokalizacja/sms/połączenia'"

def get_phone_status() -> Dict[str, Any]:
    """Zwraca pełny status telefonu dla AI."""
    status = {
        "permissions": load_permissions(),
        "device_info": {},
        "connectivity": {},
        "storage": {},
        "power": {}
    }
    
    try:
        # Informacje o urządzeniu
        device_info = subprocess.check_output(["getprop"], timeout=5).decode()
        status["device_info"] = {"raw": device_info[:500]}
    except:
        pass
    
    try:
        # Informacje o baterii
        battery = json.loads(subprocess.check_output(["termux-battery-status"], timeout=5))
        status["power"] = battery
    except:
        pass
    
    try:
        # Informacje o WiFi
        wifi = json.loads(subprocess.check_output(["termux-wifi-connectioninfo"], timeout=5))
        status["connectivity"]["wifi"] = wifi
    except:
        pass
    
    return status

# === FUNKCJE POMOCNICZE DLA INNYCH MODUŁÓW ===

def ai_can_use_phone() -> bool:
    """Sprawdza czy AI ma uprawnienia do używania telefonu."""
    perms = load_permissions()
    return any(perms.values())

def get_phone_capabilities() -> List[str]:
    """Zwraca listę dostępnych funkcji telefonu."""
    return [
        "📸 Robienie zdjęć", "📍 Lokalizacja GPS", "📞 Dzwonienie", 
        "💬 Wysyłanie SMS", "📋 Kontakty", "📁 Przeglądanie plików",
        "🔔 Powiadomienia", "🎤 Nagrywanie audio", "📶 Bluetooth/WiFi",
        "📱 Sensory urządzenia", "🔋 Status baterii", "📋 Schowek"
    ]

def emergency_phone_access() -> str:
    """Funkcja awaryjna - przywraca pełny dostęp AI do telefonu."""
    default_perms = {
        "camera": True, "location": True, "sms": True, "calls": True,
        "contacts": True, "files": True, "notifications": True, 
        "bluetooth": True, "wifi": True, "microphone": True,
        "sensors": True, "battery": True, "system_info": True,
        "internet": True, "storage": True, "clipboard": True
    }
    save_permissions(default_perms)
    return "🚨 PRZYWRÓCONO PEŁNY DOSTĘP AI DO TELEFONU!"
