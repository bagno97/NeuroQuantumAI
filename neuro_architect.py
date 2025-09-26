
"""
neuro_architect.py
------------------
This module defines the NeuroArchitect class, responsible for analyzing conversation history to extract frequent topics and dynamically generate Python modules for those topics.
Part of the NeuroQuantumAI Android app project.
"""

import os
import json
from typing import List, Dict, Any


class NeuroArchitect:
    """
    The NeuroArchitect analyzes conversation logs to identify frequent topics and can generate new Python modules for those topics.
    """
    def __init__(self, log_path: str = "conversation_history.json") -> None:
        """
        Initialize the NeuroArchitect.
        Args:
            log_path (str): Path to the conversation history JSON file.
        """
        self.log_path = log_path

    def analyze_topics(self) -> List[str]:
        """
        Analyze the conversation log and extract frequently mentioned topics (words).
        Returns:
            List[str]: List of words that appear at least 3 times in user input.
        """
        if not os.path.exists(self.log_path):
            return []
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"[NeuroArchitect] Error reading log file: {e}")
            return []

        topic_counter: Dict[str, int] = {}
        for entry in data:
            user_input = entry.get("user", "")
            keywords = user_input.lower().split()
            for word in keywords:
                topic_counter[word] = topic_counter.get(word, 0) + 1

        frequent = [word for word, count in topic_counter.items() if count >= 3]
        return frequent

    def build_module(self, topic: str) -> str:
        """
        Dynamically create a Python module for a given topic if it does not already exist.
        Args:
            topic (str): The topic for which to create a module.
        Returns:
            str: Status message about module creation.
        """
        filename = f"module_{topic}.py"
        if os.path.exists(filename):
            return f"Moduł {filename} już istnieje."
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(f"""# Moduł analizy tematu: {topic}\n\ndef analyze(input):\n    # Tu dodaj logikę analizy\n    pass\n""")
            return f"Utworzono nowy moduł: {filename}"
        except IOError as e:
            return f"Błąd podczas tworzenia modułu {filename}: {e}"

    def evolve(self) -> List[str]:
        """
        Analyze topics and create modules for each frequent topic.
        Returns:
            List[str]: Status messages for each attempted module creation.
        """
        topics = self.analyze_topics()
        results = []
        for topic in topics:
            results.append(self.build_module(topic))
        return results
