import unittest
from git_parser import GitParser

class TestGitParser(unittest.TestCase):
    def test_get_commits(self):
        parser = GitParser("D:/PYTHON/commit-parser", "2022-01-01")
        commits = parser.get_commits()
        self.assertIsInstance(commits, list)
        self.assertTrue(all(isinstance(commit, tuple) for commit in commits))
