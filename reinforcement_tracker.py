
def track_reinforcement(user_text: str, response: str = "") -> None:
    """
    Wzmacnia temat na podstawie tekstu użytkownika (prosta heurystyka: każde słowo >3 znaki).
    """
    tracker = ReinforcementTracker()
    for word in user_text.split():
        if len(word) > 3:
            tracker.reinforce(word.lower())

"""
reinforcement_tracker.py
-----------------------
This module defines the ReinforcementTracker class for tracking and updating reinforcement strengths for topics.
Part of the NeuroQuantumAI Android app project.
"""

import json
from typing import Dict, Any

class ReinforcementTracker:
    """
    Tracks reinforcement strengths for topics and persists them to a JSON file.
    """
    def __init__(self, db_path: str = "reinforcement.json") -> None:
        """
        Initialize the tracker and load strengths from file.
        Args:
            db_path (str): Path to the reinforcement JSON file.
        """
        self.db_path = db_path
        self.strength: Dict[str, int] = self.load()

    def load(self) -> Dict[str, int]:
        """
        Load reinforcement strengths from the JSON file.
        Returns:
            Dict[str, int]: Mapping of topic to reinforcement strength.
        """
        try:
            with open(self.db_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            print(f"[ReinforcementTracker] Error decoding JSON: {e}")
            return {}

    def reinforce(self, topic: str) -> None:
        """
        Increase the reinforcement strength for a given topic.
        Args:
            topic (str): The topic to reinforce.
        """
        self.strength[topic] = self.strength.get(topic, 0) + 1
        self.save()

    def get_strength(self, topic: str) -> int:
        """
        Get the reinforcement strength for a topic.
        Args:
            topic (str): The topic to query.
        Returns:
            int: The current strength value.
        """
        return self.strength.get(topic, 0)

    def save(self) -> None:
        """
        Save the current strengths to the JSON file.
        """
        try:
            with open(self.db_path, 'w', encoding='utf-8') as f:
                json.dump(self.strength, f, indent=4)
        except IOError as e:
            print(f"[ReinforcementTracker] Error saving file: {e}")
