import toml
from git_parser import GitParser
from plantuml_generator import PlantUMLGenerator
from visualizer import Visualizer

def main():
    config = toml.load("config.toml")["settings"]

    repo_path = config["repository_path"]
    since_date = config["since_date"]
    visualizer_path = config["visualizer_path"]

    git_parser = GitParser(repo_path, since_date)
    commits = git_parser.get_commits()

    puml_generator = PlantUMLGenerator(commits)
    puml_text = puml_generator.generate_puml()

    visualizer = Visualizer(visualizer_path)
    visualizer.render_puml(puml_text)


if __name__ == "__main__":
    main()
