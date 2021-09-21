import logging


class Util:

    @staticmethod
    def is_not_blank(s):
        return bool(s and not s.isspace())
