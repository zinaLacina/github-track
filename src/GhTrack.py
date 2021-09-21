from typing import List

from src.EmailHandler import EmailHandler
from src.GhTrackObject import GhTrackObject, EmailConf, Repo, Auth

from src.RequestInit import RequestInit


class GhTrack(GhTrackObject):
    """Class to pull down the pull request of a github public repositories for a user."""

    def __init__(self, file_name=None, token=None, email=None, user=None, repo=None):
        """Constructor.
            Email uses to send the alert notification.
            User is the repo owner(it can be a user or organisation)
            Repo is the name of the public repo we want to pull down the pull requests.
            :param email: Person to send notification .
            :param user: Github user or organization.
            :param repo: Github public repo.
        """
        super().__init__(filename=file_name)
        self.alertEmail = self.emailConf if email is None else EmailConf(to=email)
        self.repoInfos = self.repoConf if user is None or repo is None else Repo(user=user, repo=repo)
        self.authToken = self.authToken if token is None else Auth(token=token)
        self.public_repo = self.__user_repo(self.repoInfos)
        self.ghRequest = RequestInit(token=self.authToken.token)
        self.age = 7
        self.emailNotConsole = False
        self.emailHandler = EmailHandler()

    """
        This method build the full name of the public repository :owner/:reponame
        :param number: :class:`src.GhTrackObject.Repo`
        :rtype: `str`
    """

    def __user_repo(self, repo: Repo):
        return f"{repo.user}/{repo.repo}"

    """
    This method return the public repo from the config file and that you passed during the object creation
    :rtype: :class:`str`
    """

    def getRepo(self):
        return self.ghRequest.dataRequest(url=self.public_repo)

    """
    This method retrieves an all pull requests younger than the age provided, by default it 7 days
    :rtype: :class:`List[dict]`
    """

    def getPulls(self):
        return self.ghRequest.dataRequest(url=f"{self.public_repo}/pulls", old=self.age)

    """
    This method retrieves an individual pull request by it number
    :param number: int
    :rtype: :class:`dict`
    """

    def getPull(self, number):
        # / repos /: owner /:repo / pulls /: number
        assert number is not None
        return self.ghRequest.dataRequest(url=f"{self.public_repo}/pulls/{number}")

    """
    This method sets the age of the pull requests to retrieve, by default it is 7 days
    :param age: int
    :rtype: :class:`None`
    """

    def setAge(self, age: int):
        self.age = age

    """
    This method is to set the type of alert either by email or to show in the console
    :param email: bool
    :rtype: :class:`None`
    """

    def setEmailNotConsole(self, email=True):
        self.emailNotConsole = email

    """
    This method builds the summary to be sent by email or to print on the conssole
    :param pullRequests: List[dict]
    :rtype: str
    """

    def getSummary(self, pullRequests: List[dict]) -> str:
        output = ""
        for v in pullRequests:
            content = f""""
                <h1><a href="{v["html_url"]}">{v['title']} - state: {v['state']}<a></h1>
                <p><strong>Open date:<strong>{v["created_at"]}<p> 
            """
            output += content
        return output

    """
    This method send the summary to be sent by email
    :param pullRequests: List[dict]
    :rtype: str
    """
    def sendEmail(self, content: str):
        return self.emailHandler.sendEmail(content)



# if __name__ == '__main__':
#     params = "created=2021-08-30..2021-09-01"
#     g = GhTrack()
#     g.setAge(0)
#     res = g.getPulls()
#     summary = g.getSummary(res)
#     print(g.emailHandler.sendGridApi)
#     print(g.sendEmail(summary))
