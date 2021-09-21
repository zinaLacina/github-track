import json
from urllib import parse
import requests

from src.GhTrackException import UnknownApiQueryException
from src.Util import Util


class RequestInit:
    """This class inittialize the requests object with default and required values"""

    def __init__(self, token, apiUrl="https://api.github.com/repos/"):
        self.__tokenHeader = {
            "Accept": "application/vnd.github.v3+json"
        }
        if token:
            self.__tokenHeader["Authorization"] = f"token {token}"
        self.__apiUrl = apiUrl

    def dataRequest(self, url, parameters=None, body=""):
        if parameters is None:
            parameters = dict()

        headers, output = self.__statusCheckedRequest(url, parameters, body)

        page = 2
        while "link" in headers and "next" in headers["link"]:
            parameters["page"] = page
            headers, newOutput = self.__statusCheckedRequest(url, parameters, body)
            output += newOutput
            page += 1

        return output

    def __statusCheckedRequest(self, url, parameters, input):
        status, headers, output = self.__jsonRequest(url, parameters, input)
        if status < 200 or status >= 300:
            raise UnknownApiQueryException(status, output, headers)
        return headers, output

    def statusRequest(self, url, parameters, input):
        status, headers, output = self.__jsonRequest(url, parameters, input)
        return status

    def __jsonRequest(self, url, parameters, input):
        fullUrl = self.getCompleteUrl(url, parameters)
        response = requests.get(
            url=fullUrl,
            headers=self.__tokenHeader,
            data=json.dumps(input)
        )
        status = response.status_code
        headers = dict(response.headers)
        output = response.json()

        return status, headers, output

    def getCompleteUrl(self, url, parameters=None):
        if parameters is None or len(parameters) == 0:
            return f"{self.__apiUrl}{url}"
        else:
            return url + "?" + parse.urlencode(parameters)

    def getToken(self):
        return self.__tokenHeader


