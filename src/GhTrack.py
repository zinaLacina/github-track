from src.GhTrackException import RepoNotFoundException
from src.GhTrackObject import GhTrackObject, EmailConf, Repo
import requests

from src.RequestInit import RequestInit


class GhTrack(GhTrackObject):
    """Class to pull down the pull request of a github public repositories for a user."""

    def __init__(self, file_name=None, email=None, user=None, repo=None):
        """Constructor.
            Email uses to send the alert notification.
            User is the repo owner(it can be a user or organisation)
            Repo is the name of the public repo we want to pull down the pull requests.
            :param email: Person to send notification .
            :param user: Github user or organization.
            :param repo: Github public repo.
        """
        super().__init__(filename=file_name)
        self.ghRequest = RequestInit(token=self.token.token)
        self.alertEmail = self.emailConf if email is None else EmailConf(to=email)
        self.repoInfos = self.repoConf if user is None and repo is None else Repo(user=user, repo=repo)
        self.public_repo = self.__user_repo(self.repoInfos)

    def __user_repo(self, repo: Repo):
        return f"{repo.user}/{repo.repo}"


if __name__ == '__main__':
    g = GhTrack()
    print(g.ghRequest.getCompleteUrl(g.public_repo))
    print(g.ghRequest.getToken())
    res = g.ghRequest.dataRequest(url=g.public_repo)
    print(res)
