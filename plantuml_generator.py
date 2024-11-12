class PlantUMLGenerator:
    def __init__(self, commits):
        self.commits = commits

    def generate_puml(self):
        lines = ["@startuml", "digraph G {"]

        for commit, parents in self.commits:
            for parent in parents:
                lines.append(f'"{commit}" -> "{parent}"')
            if not parents:
                lines.append(f'"{commit}"')

        lines.append("}")
        lines.append("@enduml")
        return "\n".join(lines)
