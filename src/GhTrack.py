from src.GhTrackException import RepoNotFoundException
from src.GhTrackObject import GhTrackObject, EmailConf, Repo
import requests


class GhTrack(GhTrackObject):
    """Class to pull down the pull request of a github public repositories for a user."""

    def __init__(self, file_name="", email=None, user=None, repo=None):
        """Constructor.
            Email uses to send the alert notification.
            User is the repo owner(it can be a user or organisation)
            Repo is the name of the public repo we want to pull down the pull requests.
            :param email: Person to send notification .
            :param user: Github user or organization.
            :param repo: Github public repo.
        """
        super().__init__()
        self.base_url = "https://api.github.com"
        self.headers = {
            "Accept": "application/vnd.github.v3+json",
            "Authorization": f"token {self.token}"
        }
        self.alertEmail = self.emailConf if email is None else EmailConf(to=email)
        self.repoInfos = self.repoConf if user is None and repo is None else Repo(user=user, repo=repo)



    def __make_full_url(self, repo: Repo):
        return f"{self.base_url}/repos/{repo.user}/{repo.repo}"


if __name__ == '__main__':
    g = GhTrack(user="zinaLacina", repo="mutualBookstore")
