# Extracting reddit comments

import praw
from praw.models import MoreComments
        
def removing_MoreComments1(reddit_url):
    """(str) -> NoneType
    This method demonstrates how MoreComments type objects are ignored. And prints only the first level comments"""
    submission = reddit.submission(url=reddit_url)
    number = 0
    
    for top_level_comment in submission.comments:
        if isinstance(top_level_comment, MoreComments):
            continue
        number += 1
        print(top_level_comment.body, number)
        
def removing_MoreComments2(reddit_url):
    """(str) -> NoneType
    This method demonstrates how MoreComments type objects are ignored. And prints only the first level comments"""
    submission = reddit.submission(url=reddit_url)
    submission.comments.replace_more(limit = 0)
    number = 0
    
    for top_level_comment in submission.comments:
        number += 1
        print(top_level_comment.body, number)

def replace_MoreComments1(reddit_url):
    """(str) -> NoneType
    This method demonstrates how MoreComments type objects are replace. And prints only the first level comments"""
    submission = reddit.submission(url=reddit_url)
    submission.comments.replace_more(limit = None)
    number = 0
    
    for top_level_comment in submission.comments:
        number += 1
        print(top_level_comment.body, number)
        
def replace_MoreComments2(reddit_url):
    """(str) -> NoneType
    This method demonstrates how MoreComments type objects are replace. And prints the first and second-level (replies) comments"""
    submission = reddit.submission(url=reddit_url)
    submission.comments.replace_more(limit = None)
    number = 0
    
    for top_level_comment in submission.comments:
        number += 1
        print(top_level_comment.body, number)
        
        # interacting with it's CommentForest
        # each top level comment contains it's own CommentForest of replies
        for second_level_comment in top_level_comment.replies:
            #printing replies
            number += 1
            print(second_level_comment.body, number)

def replace_MoreComments_all_levels(reddit_url):
    """(str) -> NoneType
    This method demonstrates how MoreComments type objects are replace. But this time prints the entire tree
    i.e. comments on all levels (replies to replies to replies .... Try not to use this function since my app crashes"""
    
    submission = reddit.submission(url=reddit_url)
    number = 0
    
    submission.comments.replace_more(limit=None)
    
    # prints comments on all levels
    for comment in submission.comments.list():
        number += 1
        print(comment.body)

def replace_MoreComments(submission):
    """(str) -> NoneType
    This method demonstrates how MoreComments type objects are replace. And prints the first and second-level (replies) comments"""
    
    submission.comments.replace_more(limit = None)
    number1 = 0
    number2 = 0
    number3 = 0
    
    for top_level_comment in submission.comments:
        number1 += 1
        print(number1)
        
        for second_level_comment in top_level_comment.replies:
            number2 += 1
            print(second_level_comment, number2)
            
            for third_level_comment in second_level_comment.replies:
                number3 += 1
                print(third_level_comment.body, number3)
                
        #        for fourth_level_comment in third_level_comment.replies:
        #            number += 1
        #            print(fourth_level_comment.body, number)
        

if __name__ == '__main__':
    reddit = praw.Reddit('bot', config_interpolation="basic")
    
    # extracting commnets with praw for a given submission
    reddit_url = "https://www.reddit.com/r/ShingekiNoKyojin/comments/tpe5ku/half_this_sub_after_moviepart3_gets_announced/"
    submission = reddit.submission(url=reddit_url)
    # could also search through the id submission
    
    replace_MoreComments2(reddit_url)