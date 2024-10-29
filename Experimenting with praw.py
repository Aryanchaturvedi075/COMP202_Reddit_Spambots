# experimenting around with praw
import praw
from reddit import *

if __name__ == '__main__':
    reddit = praw.Reddit('bot', config_interpolation="basic")
    # url = 'https://www.reddit.com/r/csssmu/comments/tra0o1/tester/'
    # url = 'https://www.reddit.com/r/csssmu/comments/tqqga0/only_a_few_commment/'
    # url = 'https://www.reddit.com/r/csssmu/comments/tpzwyd/dont_crowd_this_plz/'
    url = 'https://www.reddit.com/r/csssmu/comments/tq0fs0/aight_here_we_go_again/'
    subreddit = reddit.subreddit("csssmu")
    replace_limit = 0
    username_string = 'stalinisabot'
    bot_daemon(reddit, url, replace_limit, subreddit, username_string)