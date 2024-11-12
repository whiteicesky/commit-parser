import subprocess
import os

class Visualizer:
    def __init__(self, visualizer_path):
        self.visualizer_path = visualizer_path
        self.java_path = r"C:\Program Files\Java\jdk-23\bin\java.exe"  # Убедитесь, что это правильный путь

    def render_puml(self, puml_text):
        with open("output.puml", "w") as f:
            f.write(puml_text)

        # Убедимся, что путь к файлу правильный
        print("Используемый путь к plantuml.jar:", os.path.abspath(self.visualizer_path))

        # Запуск PlantUML с указанием полного пути к java и plantuml.jar
        command = [r"C:\Program Files\Java\jdk-23\bin\java.exe", "-jar", os.path.abspath(self.visualizer_path), "output.puml"]

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print("Ошибка выполнения команды:", e)
        except FileNotFoundError as e:
            print("Не найден указанный файл:", e)

            # Проверка, было ли изображение успешно создано
        if os.path.exists("output.jpg"):
            print(f"Изображение успешно создано: {os.path.abspath('output.jpg')}")
            #os.startfile("output.jpg")
        else:
            print("Не удалось создать изображение.")

