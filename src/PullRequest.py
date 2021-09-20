class PullRequest:
    """
        PullRequest class is to provide summary of information on the statuses of pull requests.
        The API doc can be found here https://docs.github.com/en/rest/reference/pulls
    """

    def __repr__(self):
        return self.get__repr__(
            {"number": self._number.value, "title": self._title.value}
        )