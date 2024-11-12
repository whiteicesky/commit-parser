import subprocess
import os

class Visualizer:
    def __init__(self, plantuml_path):
        self.plantuml_path = plantuml_path

    def render_puml(self, puml_text):
        with open("temp.puml", "w") as f:
            f.write(puml_text)

        command = ["java", "-jar", self.plantuml_path, "temp.puml"]
        subprocess.run(command)
        os.remove("temp.puml")
