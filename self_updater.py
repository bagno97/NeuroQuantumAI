# self_updater.py

import os
import traceback
import json
from datetime import datetime

"""
self_updater.py
---------------
This module defines the SelfUpdater class for safe, logged, and modular code self-updating operations.

Part of the NeuroQuantumAI Android app project.
"""

from typing import Any

class SelfUpdater:
	"""
	Provides methods for appending, inserting, and creating code modules with backup and logging.
	"""
	def append_to_file(self, file_path: str, code_snippet: str) -> None:
		"""
		Append a code snippet to a file, backup the original, and log the update.
		Args:
			file_path (str): Path to the file to update.
			code_snippet (str): Code to append.
		"""
		try:
			self.backup_file(file_path)
			with open(file_path, "a", encoding="utf-8") as f:
				f.write("\n# === AI Update ===\n" + code_snippet + "\n")
			print(f"[AI] Plik zaktualizowany: {file_path}")
			self.log_update(file_path, "append", code_snippet)
		except Exception as e:
			print("Błąd aktualizacji:", e)
			traceback.print_exc()

	def create_new_module(self, module_name: str, code_content: str) -> None:
		"""
		Create a new Python module with the given code content and log the creation.
		Args:
			module_name (str): Name of the new module (without .py).
			code_content (str): Code to write to the new module.
		"""
		try:
			filename = f"{module_name}.py"
			with open(filename, "w", encoding="utf-8") as f:
				f.write(code_content)
			print(f"[AI] Utworzono nowy moduł: {filename}")
			self.log_update(filename, "create", code_content)
		except Exception as e:
			print("Błąd tworzenia modułu:", e)
			traceback.print_exc()

	def insert_code_in_file(self, file_path: str, marker: str, code_snippet: str) -> None:
		"""
		Insert a code snippet after a marker in a file, backup the original, and log the update.
		Args:
			file_path (str): Path to the file to update.
			marker (str): Marker string to search for.
			code_snippet (str): Code to insert after the marker.
		"""
		try:
			self.backup_file(file_path)
			with open(file_path, "r", encoding="utf-8") as f:
				content = f.read()
			if marker not in content:
				print(f"[AI] Marker '{marker}' nie został znaleziony w {file_path}")
				return
			updated = content.replace(marker, marker + "\n" + code_snippet)
			with open(file_path, "w", encoding="utf-8") as f:
				f.write(updated)
			print(f"[AI] Kod wstawiony w {file_path}")
			self.log_update(file_path, "insert", code_snippet)
		except Exception as e:
			print("Błąd wstawiania kodu:", e)
			traceback.print_exc()

	def log_update(self, file_path: str, action: str, code_snippet: str) -> None:
		"""
		Log an update action to update_log.json.
		Args:
			file_path (str): Path to the file updated.
			action (str): Action performed (append, create, insert).
			code_snippet (str): Code involved in the update.
		"""
		log_entry = {
			"file": file_path,
			"action": action,
			"timestamp": datetime.utcnow().isoformat() + "Z",
			"code_snippet": code_snippet
		}
		try:
			if os.path.exists("update_log.json"):
				with open("update_log.json", "r", encoding="utf-8") as log_file:
					logs = json.load(log_file)
			else:
				logs = []

			logs.append(log_entry)

			with open("update_log.json", "w", encoding="utf-8") as log_file:
				json.dump(logs, log_file, indent=2, ensure_ascii=False)
		except Exception as e:
			print("Błąd logowania aktualizacji:", e)
			traceback.print_exc()

	def backup_file(self, file_path: str) -> None:
		"""
		Create a backup of the given file.
		Args:
			file_path (str): Path to the file to backup.
		"""
		try:
			if not os.path.exists(file_path):
				print(f"[AI] Plik nie istnieje, brak kopii: {file_path}")
				return
			backup_path = file_path + ".bak"
			with open(file_path, "r", encoding="utf-8") as original:
				content = original.read()
			with open(backup_path, "w", encoding="utf-8") as backup:
				backup.write(content)
			print(f"[AI] Utworzono kopię zapasową: {backup_path}")
		except Exception as e:
			print("Błąd tworzenia kopii zapasowej:", e)
			traceback.print_exc()
