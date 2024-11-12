import subprocess
from datetime import datetime

class GitParser:
    def __init__(self, repo_path, since_date):
        self.repo_path = repo_path
        self.since_date = since_date

    def get_commits(self):
        command = [
            "git", "-C", self.repo_path, "log",
            "--since", self.since_date,
            "--pretty=format:%H %P"
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError("Failed to get git log.")

        commits = []
        for line in result.stdout.strip().split("\n"):
            parts = line.split()
            commit = parts[0]
            parents = parts[1:]
            commits.append((commit, parents))

        return commits
