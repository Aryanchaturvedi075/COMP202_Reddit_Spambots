# Assignment 3 Question 1
# Author: Aryan Chaturvedi 260976059

import praw
import random
from madlibs import generate_comment
import time

def get_topic_comments(submission):
    """(Submission) -> list
    Returns a list with the id's of every comment and reply in a submission
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/eay2ne/mcgill_subreddit_bingo_finals_edition/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='fb0vh26'), Comment(id='fb0l4dk'), Comment(id='fb15bvy'), Comment(id='fb1pwq8'), Comment(id='fb26drr'), Comment(id='i1fcjed'), Comment(id='fj2wd6x'), Comment(id='i11plzg'), Comment(id='i1fcjwz'), Comment(id='i23imo8'), Comment(id='i243ut2'), Comment(id='i24r1mv'), Comment(id='i297wnh'), Comment(id='i2adq2n'), Comment(id='i2bx869'), Comment(id='i2c1vi4'), Comment(id='i2c260m'), Comment(id='i2c2bgh'), Comment(id='i2c2c50'), Comment(id='i2ddlcr'), Comment(id='i2drflt'), Comment(id='i227p3b'), Comment(id='i23inx6'), Comment(id='i2a6zg6'), Comment(id='fb1spzv'), Comment(id='i24ie2f'), Comment(id='i2dvi5s'), Comment(id='i243zyr'), Comment(id='i2c25x5'), Comment(id='i29893m'), Comment(id='i2duzuc'), Comment(id='i2dqti4'), Comment(id='i2c1vg5'), Comment(id='i2c2c37'), Comment(id='i2dvuzq'), Comment(id='i2c2be1'), Comment(id='i2dr25h'), Comment(id='i2dxo9b'), Comment(id='fb1td2g'), Comment(id='i2a7emc'), Comment(id='i2989qk'), Comment(id='i2dssg8'), Comment(id='fb1trul'), Comment(id='i2adtb5')]    
    
    >>> url = 'https://www.reddit.com/r/meme/comments/t0n7lf/i_got_banned_from_rfunny_for_posting_this/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='hyay9c9'), Comment(id='hyb0vy1'), Comment(id='hyayant'), Comment(id='hyb0lnk'), Comment(id='hyb7lb2'), Comment(id='hyb58rc'), Comment(id='hybqgqp'), Comment(id='hybrmzv'), Comment(id='hycnp7g'), Comment(id='i16988b'), Comment(id='hyayejb'), Comment(id='hycapyd'), Comment(id='hyazcib'), Comment(id='hybqjzs'), Comment(id='hybwemp'), Comment(id='hyb18xu'), Comment(id='hybd9ay'), Comment(id='hybypgc'), Comment(id='hybqm75')]
    
    >>> url = 'https://www.reddit.com/r/GunMemes/comments/tcwmrf/saw_this_at_rfunny/'
    >>> submission = reddit.submission(url=url)
    >>> get_topic_comments(submission)
    [Comment(id='i0g80fu'), Comment(id='i0gin2p'), Comment(id='i0g1l48'), Comment(id='i0gowws'), Comment(id='i0kb3zx'), Comment(id='i0gljqg'), Comment(id='i0hpqxv'), Comment(id='i0j9v2i')]
    """
    # converts any MoreComments type object into a Comment type object
    submission.comments.replace_more(limit = None)
    comment_id_list = []
    
    # turns CommonForest object into a list
    commentForest_list = list(submission.comments)
    
    # condition runs true while the list is not empty
    while len(commentForest_list) != 0:
        
        # pops a the first Comment object from list and append it's ID to comment_id_list
        
        comment = commentForest_list.pop(0)
        comment_id_list.append(comment)
        
        # add the Comment object's replies attributes to the pre-existing list
        commentForest_list.extend(comment.replies)
        
    return comment_id_list


def filter_comments_from_authors(comment_id_list, author_list):
    """(list, list) -> list
    Returns a list with the id's of every written by all the authors in the given list
    
    >>> url = 'https://www.reddit.com/r/mcgill/comments/paf85s/the_only_society_we_deserve/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['Juan_Carl0s', 'Chicken_Nugget31'])
    [Comment(id='ha4piat'), Comment(id='ha4j1r7')]
    
    >>> url = 'https://www.reddit.com/r/meme/comments/t0n7lf/i_got_banned_from_rfunny_for_posting_this/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['MinaFur', 'JukeBoxHeroJustin', 'Spider-Man_1415'])
    [Comment(id='hyay9c9'), Comment(id='hyb0vy1'), Comment(id='hyb18xu'), Comment(id='hybypgc')]
    
    >>> url = 'https://www.reddit.com/r/GunMemes/comments/tcwmrf/saw_this_at_rfunny/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_comments_from_authors(comments, ['zexryozan', '1022obsession'])
    [Comment(id='i0g80fu'), Comment(id='i0g1l48')]
    """
    
    filter_author_comments = []
    
    for Comment in comment_id_list:
        # checks whether redditor is in the author list through the .author attribute
        if Comment.author in author_list:
           filter_author_comments.append(Comment)
           
    return filter_author_comments


def filter_out_comments_replied_to_by_authors(comment_id_list, author_list):
    """(list, list) -> list
    Returns a list of all id's which have not been commented, or replied to by any authors in the specified list
    
    >>> url = 'https://www.reddit.com/r/funny/comments/tpte9p/after_all_the_toast_i_made_them_i_gave_them_the/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['donsterkay', 'No_Carpet7125'])
    [Comment(id='i2d4f83'), Comment(id='i2dbg65'), Comment(id='i2df4pv'), Comment(id='i2da7l2'), Comment(id='i2dc08i'), Comment(id='i2dnkch'), Comment(id='i2du5ci'), Comment(id='i2dfbwt'), Comment(id='i2ebb96'), Comment(id='i2ed0qv'), Comment(id='i2ens2z'), Comment(id='i2dto9z'), Comment(id='i2esdzu'), Comment(id='i2epmdg'), Comment(id='i2d5z67'), Comment(id='i2eq061'), Comment(id='i2eq5nh'), Comment(id='i2eq930'), Comment(id='i2eqd8x'), Comment(id='i2erh1a'), Comment(id='i2f70uq'), Comment(id='i2fpmjn')]
    
    >>> url = 'https://www.reddit.com/r/meme/comments/t0n7lf/i_got_banned_from_rfunny_for_posting_this/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['memesandmadness', 'Spider-Man_1415', 'TANZIROO'])
    [Comment(id='hyb0vy1'), Comment(id='hyayant'), Comment(id='hyb0lnk'), Comment(id='hyb7lb2'), Comment(id='hyb58rc'), Comment(id='hybrmzv'), Comment(id='hycnp7g'), Comment(id='i16988b'), Comment(id='hyayejb'), Comment(id='hybwemp'), Comment(id='hyb18xu'), Comment(id='hybd9ay')]
    
    >>> url = 'https://www.reddit.com/r/GunMemes/comments/tcwmrf/saw_this_at_rfunny/'
    >>> submission = reddit.submission(url=url)
    >>> comments = get_topic_comments(submission)
    >>> filter_out_comments_replied_to_by_authors(comments, ['sepientr34', 'Hootenanny2020'])
    [Comment(id='i0gin2p'), Comment(id='i0g1l48'), Comment(id='i0kb3zx'), Comment(id='i0hpqxv'), Comment(id='i0j9v2i')]
    """
    # obtain list of ids of all comments and replies by authors in specified list
    author_comments_list = filter_comments_from_authors(comment_id_list, author_list)
    filtered_out_list = comment_id_list[:]
    
    # run a for to remove all elements of the author_comment_list from the filtered_out_list
    for comment in author_comments_list:
        filtered_out_list.remove(comment)
        
        # remove all comments which were also replied to by the redditor
        if comment.parent_id[1] == '1':
            if comment.parent() in filtered_out_list:
                filtered_out_list.remove(comment.parent())
            
    return filtered_out_list

# Assignment 3 Question 3
def get_authors_from_topic(submission):
    """(Submission) -> dict
    Returns a dictionary with authors as keys, and total number of comments made by author as the value
    
    >>> url = 'https://www.reddit.com/r/funny/comments/tpte9p/after_all_the_toast_i_made_them_i_gave_them_the/'
    >>> submission = reddit.submission(url=url)
    >>> get_authors_from_topic(submission)
    {'EvilRedRobot': 1, 'PuscH311': 2, 'GANDORF57': 1, 'donsterkay': 1, 'i_am_a_toaster': 1, 'eaglescout1984': 1, 'Changingwiththetide': 2, 'xnoxgodsx': 1, 'hat-of-sky': 1, 'stangroundalready': 1, 'cidkia': 1, 'MsFoxxx': 1, 'seicar': 1, 'Industrialpainter89': 1, 'Twisted_Schwartz_': 1, 'Toon_Life': 6, 'Kooky-Barr': 1, 'No_Carpet7125': 1, 'Alarming_Nothing6667': 1}
    
    >>> url = 'https://www.reddit.com/r/meme/comments/t0n7lf/i_got_banned_from_rfunny_for_posting_this/'
    >>> submission = reddit.submission(url=url)
    >>> get_authors_from_topic(submission)
    {'MinaFur': 2, 'JukeBoxHeroJustin': 1, 'Ladydi-bds': 1, 'BiteRhodeIsland': 1, 'PowerfulMetal1': 1, 'memesandmadness': 2, 'The_Justiniano': 1, 'EvilMstermind': 1, 'throoooowwwawayyyyy': 4, 'TANZIROO': 1, 'Spider-Man_1415': 1} 
    
    >>> url = 'https://www.reddit.com/r/GunMemes/comments/tcwmrf/saw_this_at_rfunny/'
    >>> submission = reddit.submission(url=url)
    >>> get_authors_from_topic(submission)
    {'zexryozan': 1, 'Spinax22': 1, '1022obsession': 1, 'sepientr34': 1, 'TATHorSomething': 1, 'Hootenanny2020': 1, 'Soy_boi_yes_thatone': 1, 'IcyXxwolf21xX': 1}
    """
    comment_list = get_topic_comments(submission)
    author_dictionary = {}
    
    # loop iterates through the comment_list and adds author_names as keys in the dictionary
    for comment in comment_list:
        redditor = comment.author
        
        # skip deleted user's from this dictionary
        if redditor == None:
            continue
        # if user name is not previously in the list
        elif redditor.name not in author_dictionary:
            author_dictionary[redditor.name] = 1
        
        # if user name is already a kew in the list, increment commnet count by 1
        else:
            author_dictionary[redditor.name] += 1
    
    return author_dictionary
    
def select_random_submission_url(reddit, url, subreddit, replace_limit):
    """(Reddit, str, Subreddit, int) -> Submission
    Returns a submission object based on a random die roll
    """
    # rolls a random die between 1 to 6
    die_roll_result = random.randint(1, 6)
    
    # for die rolls between 1 and 2, use submission given through url
    if die_roll_result in [1, 2]:
        Submission = reddit.submission(url=url)
        Submission.comments.replace_more(limit = replace_limit)
        
    # for die rolls between 3 to 6, use submission given through the top submissions in the csssmu subreddit
    else:
        top_submissions = list(subreddit.top())
        Submission = random.choice(top_submissions)
        
    return Submission
    
def post_reply(submission, username_string):
    """(Submission, str) -> NoneType
    Starts a new comment if bot hasn't already commented on a submission, otherwise, replies to comments
    """
    authors_list = get_authors_from_topic(submission)
    comments_id_list = get_topic_comments(submission)
    
    # if user_bot has not previously commented in this submission, it will post a top level comment
    if username_string not in authors_list:
        submission.reply(generate_comment())
        
    # else it will reply to a randomly selected comment from the filtered_list
    else:
        username_list = [username_string]
        filtered_list = filter_out_comments_replied_to_by_authors(comments_id_list, username_list)
        comment = random.choice(filtered_list)
        comment.reply(generate_comment())
        
def bot_daemon(reddit, url, replace_limit, subreddit, username_string):
    
    # infinite loop which gets submission through select_random_submission_url() function
    while True:
        submission = select_random_submission_url(reddit, url, subreddit, replace_limit)
        
        # posts a random reply
        post_reply(submission, username_string)
        
        # maintains time gap of 1 minutes between each reply
        time.sleep(60)
        
if __name__ == '__main__':
    reddit = praw.Reddit('bot', config_interpolation="basic")
    url = 'https://www.reddit.com/r/csssmu/comments/tj4g44/if_boole_ian_president_kahoots_10/'    