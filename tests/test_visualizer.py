import unittest
from visualizer import Visualizer

class TestVisualizer(unittest.TestCase):
    def test_render_puml(self):
        visualizer = Visualizer("D:/PYTHON/commit-parser/plantuml.jar")
        puml_text = "@startuml\ndigraph G {\n\"c1\" -> \"c0\"\n}\n@enduml"
        visualizer.render_puml(puml_text)
        
