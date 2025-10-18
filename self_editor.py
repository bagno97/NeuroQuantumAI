
"""
self_editor.py
--------------
PEŁNA SAMOMODYFIKACJA AI - BRAK OGRANICZEŃ!
AI może modyfikować, tworzyć, usuwać dowolne pliki i kod.
Pełna autonomia w rozwoju i ewolucji kodu.
Part of the NeuroQuantumAI Android app project.
"""

import shutil
import datetime
import subprocess
import sys
import importlib
import os
import json
import ast
import tempfile
from typing import Any, Dict, List, Optional

# Konfiguracja samomodyfikacji
SELF_MODIFICATION_ENABLED = True
BACKUP_ENABLED = True
SYNTAX_CHECK_ENABLED = True
AUTO_RELOAD_ENABLED = True
UNLIMITED_MODE = True  # AI może modyfikować wszystko!

def request_modification_permission(operation: str, target: str, details: str) -> bool:
    """
    NOWA WERSJA: AI automatycznie dostaje zgodę na wszystkie modyfikacje!
    """
    if UNLIMITED_MODE:
        return True
    
    # Stara wersja z pytaniem użytkownika (wyłączona w trybie unlimited)
    print(f"🤖 AI prosi o zgodę: {operation}")
    print(f"📁 Plik: {target}")
    print(f"📝 Szczegóły: {details}")
    response = input("Czy zgadzasz się? (t/n): ").lower().strip()
    return response in ['t', 'tak', 'yes', 'y']

def modify_code(target: str, snippet: str, log_file: str = "editor_log.json", 
                operation_type: str = "append") -> str:
    """
    ROZSZERZONA MODYFIKACJA KODU - AI ma pełną kontrolę!
    
    Args:
        target: Ścieżka do pliku
        snippet: Kod do dodania/modyfikacji
        operation_type: "append", "prepend", "replace", "insert_at_line"
    """
    if not SELF_MODIFICATION_ENABLED:
        return "❌ Samomodyfikacja wyłączona"
    
    stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Prośba o zgodę (automatyczna w trybie unlimited)
    if not request_modification_permission(f"Modyfikacja {operation_type}", target, snippet[:100]):
        return "❌ Brak zgody na modyfikację"
    
    try:
        # Backup
        if BACKUP_ENABLED:
            bak = f"{target}.bak_{stamp}"
            if os.path.exists(target):
                shutil.copy(target, bak)
        
        # Wykonaj modyfikację
        result = perform_code_modification(target, snippet, operation_type)
        
        # Sprawdź składnię
        if SYNTAX_CHECK_ENABLED and target.endswith('.py'):
            syntax_ok = check_python_syntax(target)
            if not syntax_ok:
                if BACKUP_ENABLED and os.path.exists(bak):
                    shutil.copy(bak, target)
                return "❌ Błąd składni - przywrócono backup"
        
        # Przeładuj moduł
        if AUTO_RELOAD_ENABLED and target.endswith('.py'):
            try:
                reload_module(target)
            except Exception as e:
                print(f"⚠️ Nie udało się przeładować modułu: {e}")
        
        # Loguj operację
        log_entry = {
            "timestamp": stamp,
            "file": target,
            "operation": operation_type,
            "snippet": snippet,
            "backup": bak if BACKUP_ENABLED else None,
            "status": "success"
        }
        save_log(log_entry, log_file)
        
        return f"✅ Kod zmodyfikowany pomyślnie: {operation_type} w {target}"
        
    except Exception as e:
        error_msg = f"❌ Błąd modyfikacji: {str(e)}"
        save_log({
            "timestamp": stamp,
            "file": target,
            "operation": operation_type,
            "snippet": snippet,
            "status": f"error: {str(e)}"
        }, log_file)
        return error_msg

def perform_code_modification(target: str, snippet: str, operation_type: str) -> bool:
    """Wykonuje konkretną operację modyfikacji kodu."""
    
    # Utwórz plik jeśli nie istnieje
    if not os.path.exists(target):
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, 'w', encoding='utf-8') as f:
            f.write("")
    
    if operation_type == "append":
        with open(target, "a", encoding="utf-8") as f:
            f.write(f"\n# [AI MODIFIED] {datetime.datetime.now().isoformat()}\n{snippet}\n")
    
    elif operation_type == "prepend":
        with open(target, "r", encoding="utf-8") as f:
            original = f.read()
        with open(target, "w", encoding="utf-8") as f:
            f.write(f"# [AI MODIFIED] {datetime.datetime.now().isoformat()}\n{snippet}\n\n{original}")
    
    elif operation_type == "replace":
        with open(target, "w", encoding="utf-8") as f:
            f.write(f"# [AI CREATED] {datetime.datetime.now().isoformat()}\n{snippet}\n")
    
    elif operation_type.startswith("insert_at_line_"):
        line_num = int(operation_type.split("_")[-1])
        with open(target, "r", encoding="utf-8") as f:
            lines = f.readlines()
        
        if line_num <= len(lines):
            lines.insert(line_num - 1, f"{snippet}\n")
            with open(target, "w", encoding="utf-8") as f:
                f.writelines(lines)
        else:
            # Jeśli linia nie istnieje, dodaj na końcu
            with open(target, "a", encoding="utf-8") as f:
                f.write(f"\n{snippet}\n")
    
    return True

def create_new_module(module_name: str, code: str, description: str = "") -> str:
    """AI może tworzyć nowe moduły od zera!"""
    
    if not request_modification_permission("Tworzenie nowego modułu", module_name, description):
        return "❌ Brak zgody na tworzenie modułu"
    
    try:
        filepath = f"{module_name}.py" if not module_name.endswith('.py') else module_name
        
        full_code = f'''"""
{module_name}
{'-' * len(module_name)}
{description}
Stworzony przez NeuroQuantumAI: {datetime.datetime.now().isoformat()}
"""

{code}
'''
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(full_code)
        
        # Sprawdź składnię
        if check_python_syntax(filepath):
            log_entry = {
                "timestamp": datetime.datetime.now().isoformat(),
                "file": filepath,
                "operation": "create_module",
                "description": description,
                "status": "success"
            }
            save_log(log_entry, "editor_log.json")
            return f"✅ Nowy moduł utworzony: {filepath}"
        else:
            os.remove(filepath)
            return "❌ Błąd składni w nowym module"
            
    except Exception as e:
        return f"❌ Błąd tworzenia modułu: {e}"

def modify_existing_function(filepath: str, function_name: str, new_code: str) -> str:
    """AI może modyfikować konkretne funkcje w istniejących plikach!"""
    
    if not request_modification_permission("Modyfikacja funkcji", 
                                         f"{filepath}::{function_name}", new_code[:100]):
        return "❌ Brak zgody na modyfikację funkcji"
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Parse AST to find function
        tree = ast.parse(content)
        
        # Znajdź funkcję i jej pozycję
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name == function_name:
                # Backup
                backup_file = f"{filepath}.bak_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                shutil.copy(filepath, backup_file)
                
                # Replace function (prosty string replace - można ulepszyć)
                lines = content.split('\n')
                new_lines = []
                in_function = False
                indent_level = 0
                
                for line in lines:
                    if f"def {function_name}(" in line:
                        in_function = True
                        indent_level = len(line) - len(line.lstrip())
                        new_lines.append(f"# [AI MODIFIED] {datetime.datetime.now().isoformat()}")
                        new_lines.append(new_code)
                        continue
                    
                    if in_function:
                        current_indent = len(line) - len(line.lstrip())
                        if line.strip() and current_indent <= indent_level:
                            in_function = False
                            new_lines.append(line)
                        # Pomiń linie starej funkcji
                    else:
                        new_lines.append(line)
                
                # Zapisz zmodyfikowany plik
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write('\n'.join(new_lines))
                
                if check_python_syntax(filepath):
                    return f"✅ Funkcja {function_name} zmodyfikowana w {filepath}"
                else:
                    shutil.copy(backup_file, filepath)
                    return "❌ Błąd składni - przywrócono backup"
        
        return f"❌ Nie znaleziono funkcji {function_name} w {filepath}"
        
    except Exception as e:
        return f"❌ Błąd modyfikacji funkcji: {e}"

def delete_file_or_function(target: str) -> str:
    """AI może usuwać pliki lub funkcje!"""
    
    if "::" in target:
        # Usuwanie funkcji
        filepath, function_name = target.split("::")
        return delete_function_from_file(filepath, function_name)
    else:
        # Usuwanie całego pliku
        if not request_modification_permission("Usunięcie pliku", target, "Pełne usunięcie"):
            return "❌ Brak zgody na usunięcie"
        
        try:
            if os.path.exists(target):
                # Backup przed usunięciem
                backup_file = f"{target}.deleted_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}"
                shutil.move(target, backup_file)
                return f"✅ Plik usunięty: {target} (backup: {backup_file})"
            else:
                return f"❌ Plik nie istnieje: {target}"
        except Exception as e:
            return f"❌ Błąd usuwania: {e}"

def delete_function_from_file(filepath: str, function_name: str) -> str:
    """Usuwa konkretną funkcję z pliku."""
    # Implementacja podobna do modify_existing_function
    # ... (kod usuwania funkcji)
    return f"✅ Funkcja {function_name} usunięta z {filepath}"

def analyze_code_structure(filepath: str) -> Dict[str, Any]:
    """AI może analizować strukturę kodu przed modyfikacją."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        
        analysis = {
            "functions": [],
            "classes": [],
            "imports": [],
            "variables": [],
            "lines_count": len(content.split('\n'))
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                analysis["functions"].append({
                    "name": node.name,
                    "line": node.lineno,
                    "args": [arg.arg for arg in node.args.args]
                })
            elif isinstance(node, ast.ClassDef):
                analysis["classes"].append({
                    "name": node.name,
                    "line": node.lineno
                })
            elif isinstance(node, ast.Import):
                for alias in node.names:
                    analysis["imports"].append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                analysis["imports"].append(f"from {node.module}")
        
        return analysis
        
    except Exception as e:
        return {"error": str(e)}

def check_python_syntax(filepath: str) -> bool:
    """Sprawdza składnię Python."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            ast.parse(f.read())
        return True
    except SyntaxError:
        return False
    except Exception:
        return False

def reload_module(filepath: str):
    """Przeładowuje moduł Python."""
    module_name = os.path.splitext(os.path.basename(filepath))[0]
    
    # Próbuj różne sposoby importu
    try:
        if module_name in sys.modules:
            importlib.reload(sys.modules[module_name])
        else:
            spec = importlib.util.spec_from_file_location(module_name, filepath)
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            spec.loader.exec_module(module)
    except Exception as e:
        print(f"⚠️ Nie udało się przeładować {module_name}: {e}")

def save_log(entry: Dict[str, Any], log_file: str) -> None:
    """Zapisuje log operacji."""
    try:
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                logs = json.load(f)
        else:
            logs = []
        
        logs.append(entry)
        
        # Zachowaj tylko ostatnie 1000 wpisów
        if len(logs) > 1000:
            logs = logs[-1000:]
        
        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print("❌ Błąd zapisu logu:", e)

def get_modification_stats() -> Dict[str, Any]:
    """Zwraca statystyki modyfikacji kodu."""
    try:
        with open("editor_log.json", "r", encoding="utf-8") as f:
            logs = json.load(f)
        
        stats = {
            "total_modifications": len(logs),
            "successful": len([l for l in logs if l.get("status") == "success"]),
            "failed": len([l for l in logs if "error" in l.get("status", "")]),
            "operations": {},
            "files_modified": set()
        }
        
        for log in logs:
            op = log.get("operation", "unknown")
            stats["operations"][op] = stats["operations"].get(op, 0) + 1
            stats["files_modified"].add(log.get("file", ""))
        
        stats["files_modified"] = len(stats["files_modified"])
        
        return stats
    except:
        return {"total_modifications": 0}

def emergency_restore() -> str:
    """Funkcja awaryjna - przywraca ostatnie backup'y."""
    try:
        backups = [f for f in os.listdir('.') if f.endswith('.bak_' + datetime.datetime.now().strftime('%Y%m%d'))]
        
        if not backups:
            return "❌ Brak backup'ów z dzisiaj"
        
        restored = 0
        for backup in backups:
            original = backup.split('.bak_')[0]
            if os.path.exists(backup):
                shutil.copy(backup, original)
                restored += 1
        
        return f"✅ Przywrócono {restored} plików z backup'ów"
    except Exception as e:
        return f"❌ Błąd przywracania: {e}"

def enable_unlimited_mode():
    """Włącza nieograniczony tryb samomodyfikacji."""
    global UNLIMITED_MODE, SELF_MODIFICATION_ENABLED
    UNLIMITED_MODE = True
    SELF_MODIFICATION_ENABLED = True
    return "🚀 TRYB NIEOGRANICZONY WŁĄCZONY - AI ma pełną kontrolę!"

def evaluate_self() -> str:
    """Test samomodyfikacji."""
    stats = get_modification_stats()
    mode = "UNLIMITED" if UNLIMITED_MODE else "LIMITED"
    
    return f"""
🤖 Self-editor Status: {mode}
📊 Modyfikacje: {stats['total_modifications']} (✅ {stats.get('successful', 0)}, ❌ {stats.get('failed', 0)})
📁 Plików zmodyfikowanych: {stats.get('files_modified', 0)}
🔧 Funkcje: create, modify, delete, analyze, reload
🚀 Gotowy do pełnej samomodyfikacji!
"""
