import unittest
from plantuml_generator import PlantUMLGenerator

class TestPlantUMLGenerator(unittest.TestCase):
    def test_generate_puml(self):
        commits = [("c1", ["c0"]), ("c2", ["c1"])]
        generator = PlantUMLGenerator(commits)
        puml_text = generator.generate_puml()
        self.assertIn("@startuml", puml_text)
        self.assertIn('"c1" -> "c0"', puml_text)
        self.assertIn("@enduml", puml_text)
