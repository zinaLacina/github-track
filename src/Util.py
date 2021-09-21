import logging
from datetime import datetime


class Util:

    @staticmethod
    def is_not_blank(s) -> bool:
        return bool(s and not s.isspace())

    @staticmethod
    def oneWeekOld(postDate: str, old: int) -> bool:
        post = datetime.fromisoformat(postDate[:-1])
        diffDay = (datetime.now() - post).days
        return diffDay <= old

