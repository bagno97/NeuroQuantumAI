"""
ai_extensions.py
--------------
Moduł zapewniający framework do dynamicznego rozszerzania funkcjonalności AI nawet w środowisku
z ograniczeniami dostępu do systemu plików (np. w aplikacji Android).

Ten moduł dostarcza API dla dynamicznych rozszerzeń, które mogą być instalowane, aktualizowane
i używane przez AI nawet bez dostępu do zapisu w głównym katalogu aplikacji.
"""

import os
import sys
import json
import importlib.util
from string import Template
from typing import Dict, List, Any, Callable, Optional, Union

# Importuj dynamic_loader jeśli jest dostępny
try:
    from dynamic_loader import dynamic_module_manager
except ImportError:
    dynamic_module_manager = None

# Stałe
DEFAULT_EXTENSION_DIR = "extensions"
DEFAULT_CONFIG_FILE = "extensions.json"

class Extension:
    """
    Klasa reprezentująca pojedyncze rozszerzenie AI.
    """
    def __init__(self, name: str, version: str = "0.1", description: str = "", 
                 author: str = "AI", module_path: str = None):
        """
        Inicjalizuje rozszerzenie.
        
        Args:
            name (str): Nazwa rozszerzenia
            version (str): Wersja rozszerzenia
            description (str): Opis rozszerzenia
            author (str): Autor rozszerzenia
            module_path (str): Ścieżka do modułu rozszerzenia
        """
        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.module_path = module_path
        self.module = None  # Załadowany moduł
        self.methods = {}  # Dostępne metody
        
    def load(self) -> bool:
        """
        Ładuje moduł rozszerzenia.
        
        Returns:
            bool: True jeśli załadowano moduł, False w przeciwnym razie
        """
        try:
            if dynamic_module_manager is not None:
                self.module = dynamic_module_manager.get_module(self.name)
                if self.module is not None:
                    self._scan_methods()
                    return True
            
            if self.module_path and os.path.exists(self.module_path):
                spec = importlib.util.spec_from_file_location(f"ai_extension_{self.name}", self.module_path)
                if spec is not None and spec.loader is not None:
                    self.module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(self.module)
                    self._scan_methods()
                    return True
            return False
        except Exception as e:
            print(f"[Extension] Error loading extension {self.name}: {e}")
            return False
    
    def _scan_methods(self) -> None:
        """
        Skanuje moduł w poszukiwaniu dostępnych metod.
        """
        if self.module is None:
            return
        
        for attr_name in dir(self.module):
            if attr_name.startswith("_"):
                continue
            
            attr = getattr(self.module, attr_name)
            if callable(attr):
                self.methods[attr_name] = attr
    
    def call(self, method_name: str, *args, **kwargs) -> Any:
        """
        Wywołuje metodę rozszerzenia.
        
        Args:
            method_name (str): Nazwa metody do wywołania
            *args, **kwargs: Argumenty dla metody
            
        Returns:
            Any: Wynik wywołania metody lub None w przypadku błędu
        """
        if method_name not in self.methods:
            return None
        
        try:
            return self.methods[method_name](*args, **kwargs)
        except Exception as e:
            print(f"[Extension] Error calling {self.name}.{method_name}: {e}")
            return None
    
    def to_dict(self) -> Dict[str, Any]:
        """
        Konwertuje rozszerzenie na słownik do serializacji.
        
        Returns:
            Dict[str, Any]: Słownik reprezentujący rozszerzenie
        """
        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "author": self.author,
            "module_path": self.module_path
        }

class ExtensionManager:
    """
    Zarządza rozszerzeniami AI, umożliwiając ich instalację, aktualizację i używanie.
    """
    def __init__(self, extension_dir: str = DEFAULT_EXTENSION_DIR, 
                 config_file: str = DEFAULT_CONFIG_FILE):
        """
        Inicjalizuje menedżera rozszerzeń.
        
        Args:
            extension_dir (str): Katalog z rozszerzeniami
            config_file (str): Plik konfiguracyjny rozszerzeń
        """
        self.extension_dir = extension_dir
        self.config_file = config_file
        self.extensions: Dict[str, Extension] = {}
        
        # Utwórz katalog rozszerzeń, jeśli nie istnieje
        try:
            os.makedirs(self.extension_dir, exist_ok=True)
        except Exception:
            pass
        
        # Załaduj konfigurację
        self.load_config()
        
    def load_config(self) -> None:
        """
        Ładuje konfigurację rozszerzeń z pliku.
        """
        try:
            if os.path.exists(self.config_file):
                with open(self.config_file, "r", encoding="utf-8") as f:
                    config = json.load(f)
                
                for ext_data in config.get("extensions", []):
                    ext = Extension(
                        name=ext_data.get("name", ""),
                        version=ext_data.get("version", "0.1"),
                        description=ext_data.get("description", ""),
                        author=ext_data.get("author", "AI"),
                        module_path=ext_data.get("module_path", "")
                    )
                    self.extensions[ext.name] = ext
        except Exception as e:
            print(f"[ExtensionManager] Error loading config: {e}")
    
    def save_config(self) -> None:
        """
        Zapisuje konfigurację rozszerzeń do pliku.
        """
        try:
            config = {
                "extensions": [ext.to_dict() for ext in self.extensions.values()]
            }
            
            with open(self.config_file, "w", encoding="utf-8") as f:
                json.dump(config, f, indent=2)
        except Exception as e:
            print(f"[ExtensionManager] Error saving config: {e}")
    
    def install_extension(self, name: str, code: str, description: str = "", 
                        author: str = "AI", version: str = "0.1") -> bool:
        """
        Instaluje nowe rozszerzenie.
        
        Args:
            name (str): Nazwa rozszerzenia
            code (str): Kod źródłowy rozszerzenia
            description (str): Opis rozszerzenia
            author (str): Autor rozszerzenia
            version (str): Wersja rozszerzenia
            
        Returns:
            bool: True jeśli zainstalowano rozszerzenie, False w przeciwnym razie
        """
        try:
            # Najpierw spróbuj użyć dynamic_loader
            if dynamic_module_manager is not None:
                success = dynamic_module_manager.create_module(name, code)
                if success:
                    ext = Extension(name=name, description=description, 
                                  author=author, version=version)
                    self.extensions[name] = ext
                    ext.load()
                    self.save_config()
                    return True
            
            # Jeśli nie ma dynamic_loader, użyj standardowego zapisu do pliku
            module_path = os.path.join(self.extension_dir, f"{name}.py")
            with open(module_path, "w", encoding="utf-8") as f:
                f.write(code)
            
            ext = Extension(name=name, description=description, author=author, 
                          version=version, module_path=module_path)
            self.extensions[name] = ext
            ext.load()
            self.save_config()
            return True
        except Exception as e:
            print(f"[ExtensionManager] Error installing extension {name}: {e}")
            return False
    
    def uninstall_extension(self, name: str) -> bool:
        """
        Odinstalowuje rozszerzenie.
        
        Args:
            name (str): Nazwa rozszerzenia
            
        Returns:
            bool: True jeśli odinstalowano rozszerzenie, False w przeciwnym razie
        """
        if name not in self.extensions:
            return False
        
        try:
            ext = self.extensions[name]
            if ext.module_path and os.path.exists(ext.module_path):
                os.remove(ext.module_path)
            
            # Usuń z dynamic_loader, jeśli jest dostępny
            if dynamic_module_manager is not None:
                # Tu mógłby być kod do usunięcia z dynamic_loader
                pass
            
            del self.extensions[name]
            self.save_config()
            return True
        except Exception as e:
            print(f"[ExtensionManager] Error uninstalling extension {name}: {e}")
            return False
    
    def get_extension(self, name: str) -> Optional[Extension]:
        """
        Pobiera rozszerzenie o podanej nazwie.
        
        Args:
            name (str): Nazwa rozszerzenia
            
        Returns:
            Optional[Extension]: Rozszerzenie lub None jeśli nie istnieje
        """
        if name not in self.extensions:
            return None
        
        ext = self.extensions[name]
        if ext.module is None:
            ext.load()
        
        return ext
    
    def call_extension(self, name: str, method: str, *args, **kwargs) -> Any:
        """
        Wywołuje metodę rozszerzenia.
        
        Args:
            name (str): Nazwa rozszerzenia
            method (str): Nazwa metody
            *args, **kwargs: Argumenty dla metody
            
        Returns:
            Any: Wynik wywołania metody lub None w przypadku błędu
        """
        ext = self.get_extension(name)
        if ext is None:
            return None
        
        return ext.call(method, *args, **kwargs)
    
    def list_extensions(self) -> List[Dict[str, str]]:
        """
        Zwraca listę zainstalowanych rozszerzeń.
        
        Returns:
            List[Dict[str, str]]: Lista słowników opisujących rozszerzenia
        """
        return [
            {
                "name": ext.name,
                "version": ext.version,
                "description": ext.description,
                "author": ext.author,
                "methods": list(ext.methods.keys()) if ext.module is not None else []
            }
            for ext in self.extensions.values()
        ]
    
    def load_all(self) -> int:
        """
        Ładuje wszystkie zainstalowane rozszerzenia.
        
        Returns:
            int: Liczba załadowanych rozszerzeń
        """
        loaded = 0
        for ext in self.extensions.values():
            if ext.load():
                loaded += 1
        return loaded

# Globalna instancja menedżera rozszerzeń
extension_manager = ExtensionManager()

def install_extension(name: str, code: str, description: str = "", 
                     author: str = "AI", version: str = "0.1") -> bool:
    """
    Instaluje nowe rozszerzenie.
    
    Args:
        name (str): Nazwa rozszerzenia
        code (str): Kod źródłowy rozszerzenia
        description (str): Opis rozszerzenia
        author (str): Autor rozszerzenia
        version (str): Wersja rozszerzenia
        
    Returns:
        bool: True jeśli zainstalowano rozszerzenie, False w przeciwnym razie
    """
    return extension_manager.install_extension(name, code, description, author, version)

def call_extension(name: str, method: str, *args, **kwargs) -> Any:
    """
    Wywołuje metodę rozszerzenia.
    
    Args:
        name (str): Nazwa rozszerzenia
        method (str): Nazwa metody
        *args, **kwargs: Argumenty dla metody
        
    Returns:
        Any: Wynik wywołania metody lub None w przypadku błędu
    """
    return extension_manager.call_extension(name, method, *args, **kwargs)

def list_extensions() -> List[Dict[str, str]]:
    """
    Zwraca listę zainstalowanych rozszerzeń.
    
    Returns:
        List[Dict[str, str]]: Lista słowników opisujących rozszerzenia
    """
    return extension_manager.list_extensions()

def create_sample_extension(name: str = "sample") -> bool:
    """
    Tworzy przykładowe rozszerzenie.
    
    Args:
        name (str): Nazwa rozszerzenia
        
    Returns:
        bool: True jeśli utworzono rozszerzenie, False w przeciwnym razie
    """
    code_template = Template("""# Przykładowe rozszerzenie '$name'

def process(text):
    \"\"\"
    Przetwarza tekst i zwraca odpowiedź.
    
    Args:
        text (str): Tekst do przetworzenia
        
    Returns:
        str: Odpowiedź rozszerzenia
    \"\"\"
    if "hello" in text.lower():
        return "Rozszerzenie $name mówi: Cześć!"
    return "Rozszerzenie $name aktywne."

def analyze(data):
    \"\"\"
    Analizuje dane.
    
    Args:
        data: Dane do analizy
        
    Returns:
        dict: Wynik analizy
    \"\"\"
    try:
        data_str = str(data)
    except Exception:
        data_str = "<unserializable>"
    return {
        "extension": "$name",
        "status": "ok",
        "result": "Przeanalizowano: " + data_str
    }
""")
    code = code_template.substitute(name=name)
    return install_extension(
        name=name,
        code=code,
        description=f"Przykładowe rozszerzenie {name}",
        author="AI",
        version="0.1"
    )