from src.RequestInit import RequestInit
from tests.TestInit import TestInit


class RequestInitTest(TestInit):

    def setUp(self):
        self.req = RequestInit(token="token")

    def expect(self, url, parameters, input, status, responseHeaders, output):
        pass


