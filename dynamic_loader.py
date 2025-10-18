"""
dynamic_loader.py
----------------
Ten moduł umożliwia dynamiczne ładowanie i importowanie modułów, które zostały utworzone lub zmodyfikowane
w trakcie działania programu, nawet w środowisku z ograniczeniami (np. Android).
Używa systemu "pluginów" do obejścia ograniczeń standardowego importu.
"""

import importlib.util
import sys
import os
import json
from typing import Dict, List, Any, Callable, Optional
from system_requirements import get_best_dynamic_dir

class DynamicModuleManager:
    """
    Zarządza dynamicznym tworzeniem, ładowaniem i używaniem modułów generowanych przez AI.
    """
    def __init__(self):
        """
        Inicjalizuje menedżer modułów dynamicznych.
        """
        self.dynamic_dir = get_best_dynamic_dir()
        self.modules = {}
        self.module_index = {}
        self._ensure_module_index()
        self._load_existing_modules()
        
    def _ensure_module_index(self) -> None:
        """
        Upewnia się, że plik indeksu modułów istnieje.
        """
        index_path = os.path.join(self.dynamic_dir, "module_index.json")
        if not os.path.exists(index_path):
            try:
                with open(index_path, "w", encoding="utf-8") as f:
                    json.dump({}, f)
            except Exception as e:
                print(f"[DynamicLoader] Nie można utworzyć pliku indeksu: {e}")
        else:
            try:
                with open(index_path, "r", encoding="utf-8") as f:
                    self.module_index = json.load(f)
            except Exception as e:
                print(f"[DynamicLoader] Błąd odczytu indeksu: {e}")
                self.module_index = {}
    
    def _save_module_index(self) -> None:
        """
        Zapisuje indeks modułów do pliku.
        """
        index_path = os.path.join(self.dynamic_dir, "module_index.json")
        try:
            with open(index_path, "w", encoding="utf-8") as f:
                json.dump(self.module_index, f, indent=2)
        except Exception as e:
            print(f"[DynamicLoader] Nie można zapisać indeksu: {e}")
    
    def _load_existing_modules(self) -> None:
        """
        Ładuje istniejące moduły z katalogu dynamicznego.
        """
        if not os.path.exists(self.dynamic_dir):
            return
            
        for filename in os.listdir(self.dynamic_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                self.load_module(module_name)
    
    def create_module(self, name: str, code: str) -> bool:
        """
        Tworzy nowy moduł dynamiczny.
        
        Args:
            name (str): Nazwa modułu (bez rozszerzenia .py)
            code (str): Kod źródłowy modułu
            
        Returns:
            bool: True jeśli pomyślnie utworzono moduł, False w przeciwnym razie
        """
        try:
            # Upewnij się, że katalog istnieje
            os.makedirs(self.dynamic_dir, exist_ok=True)
            
            # Zapisz moduł do pliku
            module_path = os.path.join(self.dynamic_dir, f"{name}.py")
            with open(module_path, "w", encoding="utf-8") as f:
                f.write(code)
            
            # Zaktualizuj indeks modułów
            self.module_index[name] = {
                "path": module_path,
                "timestamp": os.path.getmtime(module_path)
            }
            self._save_module_index()
            
            # Załaduj moduł
            return self.load_module(name)
        except Exception as e:
            print(f"[DynamicLoader] Błąd tworzenia modułu {name}: {e}")
            return False
    
    def load_module(self, name: str) -> bool:
        """
        Ładuje istniejący moduł dynamiczny.
        
        Args:
            name (str): Nazwa modułu (bez rozszerzenia .py)
            
        Returns:
            bool: True jeśli pomyślnie załadowano moduł, False w przeciwnym razie
        """
        try:
            module_path = os.path.join(self.dynamic_dir, f"{name}.py")
            if not os.path.exists(module_path):
                print(f"[DynamicLoader] Moduł {name} nie istnieje")
                return False
                
            # Załaduj moduł
            spec = importlib.util.spec_from_file_location(f"dynamic_{name}", module_path)
            if spec is None or spec.loader is None:
                print(f"[DynamicLoader] Nie można utworzyć spec dla {name}")
                return False
                
            module = importlib.util.module_from_spec(spec)
            sys.modules[f"dynamic_{name}"] = module
            spec.loader.exec_module(module)
            self.modules[name] = module
            
            return True
        except Exception as e:
            print(f"[DynamicLoader] Błąd ładowania modułu {name}: {e}")
            return False
    
    def update_module(self, name: str, code: str) -> bool:
        """
        Aktualizuje istniejący moduł dynamiczny.
        
        Args:
            name (str): Nazwa modułu (bez rozszerzenia .py)
            code (str): Nowy kod źródłowy modułu
            
        Returns:
            bool: True jeśli pomyślnie zaktualizowano moduł, False w przeciwnym razie
        """
        try:
            module_path = os.path.join(self.dynamic_dir, f"{name}.py")
            
            # Utwórz kopię zapasową
            if os.path.exists(module_path):
                backup_path = f"{module_path}.bak"
                with open(module_path, "r", encoding="utf-8") as src:
                    with open(backup_path, "w", encoding="utf-8") as dst:
                        dst.write(src.read())
            
            # Zapisz nową wersję
            with open(module_path, "w", encoding="utf-8") as f:
                f.write(code)
            
            # Zaktualizuj indeks
            self.module_index[name] = {
                "path": module_path,
                "timestamp": os.path.getmtime(module_path)
            }
            self._save_module_index()
            
            # Przeładuj moduł
            if name in sys.modules:
                del sys.modules[f"dynamic_{name}"]
            if name in self.modules:
                del self.modules[name]
            
            return self.load_module(name)
        except Exception as e:
            print(f"[DynamicLoader] Błąd aktualizacji modułu {name}: {e}")
            return False
    
    def get_module(self, name: str) -> Optional[Any]:
        """
        Pobiera załadowany moduł dynamiczny.
        
        Args:
            name (str): Nazwa modułu
            
        Returns:
            Optional[Any]: Załadowany moduł lub None jeśli moduł nie istnieje
        """
        if name in self.modules:
            return self.modules[name]
        else:
            loaded = self.load_module(name)
            if loaded:
                return self.modules[name]
            return None
    
    def call_function(self, module_name: str, function_name: str, *args, **kwargs) -> Any:
        """
        Wywołuje funkcję w dynamicznym module.
        
        Args:
            module_name (str): Nazwa modułu
            function_name (str): Nazwa funkcji
            *args, **kwargs: Argumenty do przekazania do funkcji
            
        Returns:
            Any: Wynik wywołania funkcji lub None w przypadku błędu
        """
        module = self.get_module(module_name)
        if module is None:
            print(f"[DynamicLoader] Moduł {module_name} nie istnieje")
            return None
            
        if not hasattr(module, function_name):
            print(f"[DynamicLoader] Funkcja {function_name} nie istnieje w module {module_name}")
            return None
            
        try:
            func = getattr(module, function_name)
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[DynamicLoader] Błąd wywołania {module_name}.{function_name}: {e}")
            return None
    
    def list_modules(self) -> List[str]:
        """
        Zwraca listę dostępnych modułów dynamicznych.
        
        Returns:
            List[str]: Lista nazw modułów
        """
        return list(self.module_index.keys())

# Instancja globalna dla łatwego dostępu
dynamic_module_manager = DynamicModuleManager()