import os
from dataclasses import dataclass
import yaml

import logging as log

@dataclass
class Auth:
    token: str = ""


@dataclass
class EmailConf:
    to: str = "zinalacina@gmail.com"
    subject: str = "Pull request Test"


@dataclass
class Repo:
    user: str = "kubernetes"
    repo: str = "kubernetes"


@dataclass
class GhTrackObject:
    filename: str
    emailConf: EmailConf = EmailConf()
    repoConf: Repo = Repo()
    authToken: Auth = Auth()

    def __post_init__(self):
        self.emailConf, self.repoConf, self.authToken = self.getConf(self.filename)

    def getConf(self, file_name: str) -> (EmailConf, Repo, Auth):
        if not file_name:
            file_name = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data/config.yml")
        try:
            with open(file_name) as f:
                setting = yaml.safe_load(f)["settings"]
                token = Auth(setting["github"]["token"])
                email = EmailConf(to=setting["email"]["to"], subject=setting["email"]["subject"])
                repo = Repo(user=setting["repo"]["user"], repo=setting["repo"]["name"])
                return email, repo, token
        except:
            log.info(f"impossible to open file {file_name}")
            return EmailConf(), Repo(), Auth()


# if __name__ == '__main__':
#     filename = "../data/config.yml"
#     gh = GhTrackObject(filename=filename)
