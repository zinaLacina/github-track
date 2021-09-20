from dataclasses import dataclass
import yaml


@dataclass
class Auth:
    token: str = "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"


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
    token: Auth = Auth()

    def __post_init__(self):
        self.emailConf, self.repoConf, self.token = self.getConf(self.filename)

    def getConf(self, file_name: str) -> (EmailConf, Repo, Auth):
        try:
            with open(file_name) as f:
                setting = yaml.safe_load(f)["settings"]
                token = Auth(setting["github"]["token"])
                email = EmailConf(to=setting["email"]["to"], subject=setting["email"]["subject"])
                repo = Repo(user=setting["repo"]["user"], repo=setting["repo"]["name"])
                return email, repo, token
        except Exception as ex:
            print(f"Unable to load file, use default values {ex}")
            return EmailConf(), Repo(), Auth()


if __name__ == '__main__':
    filename = "../data/config.yml"
    gh = GhTrackObject(filename=filename)

