import json
import os

class LevelLoader:
    def __init__(self, level_number):
        self.level_number = level_number
        self.level_files = "pacman-art/levels" #hardcode this

    def load_level(self):
        """Load level data from a JSON file."""
        level_file = f"{self.level_files}/level{self.level_number}.json"
        if not os.path.isfile(level_file):
            raise FileNotFoundError(f"Level file '{level_file}' not found.")
        
        with open(level_file, 'r') as file:
            return json.load(file)