#!/usr/bin/env python
import argparse
from colorama import Fore, Back, Style

from src.GhTrack import GhTrack

"""
github-track.commandline
~~~~~~~~~~~~~~~~~~~~~~
github-track is a module that pulls the 7 days latest github pull requests.
This module is it command line interface
Usage:
    >>> ghtrack --help
    usage: ghtrack [-h] token
    positional arguments:
      token    Github Token
    optional arguments:
      -h, --help  show this help message and exit
    >>> ghtrack <token>
    # set a token for unlimited queries.
    >>> ghtrack
    # if you dont see any token, but with a rate limit of 60.
    >>> ghtrack <reponame>
    #  pulls the 7 days latest github pull requests.
"""


class CommandLineUtil:

    @staticmethod
    def main():
        """Starting point for the program execution."""

        # Create command line parser.
        parser = argparse.ArgumentParser()

        # Adding command line arguments.
        parser.add_argument("file", help="Config file", default=None)

        # Adding command line arguments.
        parser.add_argument("token", help="Github token", default=None)

        # Adding command line arguments.
        parser.add_argument("email", help="The email to send alert", default="zinatestmail@gmail.com")

        # Adding command line arguments.
        parser.add_argument("user", help="The public repo owner", default="kubernetes")

        # Adding command line arguments.
        parser.add_argument("repo", help="The public repo", default="kubernetes")

        # Parse command line arguments.
        arguments = parser.parse_args()
        file, token, email, user, repo = arguments.file, arguments.token, arguments.email, arguments.user, arguments.repo
        print(Fore.CYAN, "With token you will have an higher rate queries")
        print(Fore.CYAN, "Skipping token may result with rate limit exception")
        print(Fore.GREEN, f"file = {file}, token = {token}, email = {email}, user = {user}, repo={repo}")
        print(Style.RESET_ALL)

        try:
            print(Style.BRIGHT)
            g = GhTrack(file_name=file, token=token, email=email, user=user, repo=repo)
            pullRequests = g.getPulls()
            if not email:
                print(Fore.GREEN, "Since you did not provide an email, here the console")
                print(Fore.RED, f"Public repo: {g.public_repo}")
                print(Fore.RED, "~~~~~~~~~~SUMMARY~~~~~~~~~")
                print(Fore.MAGENTA, f"{g.getSummary(pullRequests)}")
            else:
                print(Fore.GREEN, f"Since you provided an email, an email was sent to: {g.alertEmail.to}")
                print(Fore.RED, f"Public repo: {g.public_repo}")
                print(Fore.RED, "~~~~~~~~~~SUMMARY SENT BY EMAIL~~~~~~~~~")
                print(Fore.MAGENTA, f"{g.getSummary(pullRequests)}")
        except Exception as ex:
            print(Style.DIM)
            print(Fore.RED, f"Something went wrong during the object initialization {ex}")
            print(Style.RESET_ALL)
            exit()

