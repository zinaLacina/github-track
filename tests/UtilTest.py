from src.Util import Util
from tests.TestInit import TestInit


class UtilTest(TestInit):

    def test_is_not_blank(self):
        self.assertFalse(Util.is_not_blank(""), msg="it should be true")
        self.assertTrue(Util.is_not_blank("test"), msg="test is not blank")

    def testOneWeekOld(self):
        post = "2014-06-06T22:56:04Z"
        self.assertFalse(Util.oneWeekOld(post))