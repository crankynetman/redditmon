"""Module for monitoring a subreddit for new posts
"""

import praw, time, os, argparse, configparser

# TODO: Move all this argparse shit somewhere else.

parser = argparse.ArgumentParser(description="Monitor Reddit")
parser.add_argument(
    'Subreddit', 
    metavar='subreddit',
    type=str, 
    help='The name of the subreddit you want to view')

parser.add_argument(
    '-r', 
    metavar='refresh',
    type=int,
    default=10,
    help='The amount of time in seconds between refreshes')

parser.add_argument(
    '-c',
    metavar='config',
    type=str,
    default='config.ini',
    help='The file path to the config file')

args = parser.parse_args()

subreddit_name = args.Subreddit
refresh_interval = args.r
config_path = args.c

config = configparser.ConfigParser()
config.read(config_path)

reddit = praw.Reddit(
    client_id=config["API"]["client_id"],
    client_secret=config["API"]["client_secret"],
    user_agent=config["API"]["user_agent"]
    )

class RedditDisplay:
    def __init__(self, subreddit_name, refresh_interval):
        self.subreddit = subreddit_name
        self.refresh_interval = refresh_interval
        self.post = self.get_top_post()

    def get_top_post(self):
        post = list(reddit.subreddit(self.subreddit).hot(limit=1))[0]
        return post

    def print_post_title(self):
        print(f'The Current Top Post on /r/{self.subreddit} is:')
        print(f'"{self.post.title}" submitted by user "{self.post.author}" with {self.post.score} Upvotes')

    def print_post_body(self):
        if self.post.selftext == "":
            print(f'Click to view URL: {self.post.url}')
        else:
            print(self.post.selftext)

    def print_post_url(self):
        print(f'View This Post on Reddit at this URL: https://old.reddit.com{self.post.permalink}')

    def display_post(self):
        # Clear out the old posts from the Terminal Screen
        os.system("clear")

        # Print out the post
        self.print_post_title()
        print()
        self.print_post_body()
        print()
        self.print_post_url()

        # Hang out a bit until the refresh interval expires
        time.sleep(self.refresh_interval)
        print("Done Sleeping!")


if __name__ == __name__:
    display = RedditDisplay(subreddit_name, refresh_interval)
    while True:
        display.display_post()
