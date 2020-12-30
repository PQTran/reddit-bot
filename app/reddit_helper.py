import constants
import logging
import praw

reddit = None

def get_reddit_instance():
    global reddit
    if reddit == None:
        user_agent = "script:playing-cards-io-bot:v0.1 (by /u/pqtran)"
        reddit = praw.Reddit("redditbot", user_agent=user_agent)
    return reddit

def get_subreddit(name):
    reddit = get_reddit_instance()
    return reddit.subreddit(name)

def get_bot_redditor():
    reddit = get_reddit_instance()
    return reddit.user.me()

def notify_moderator(url):
    reddit = get_reddit_instance()
    mod_redditor = praw.models.Redditor(reddit, constants.MOD_REDDITOR_NAME)

    msg_subject = "Auto-generated message for /r/{}".format(constants.SUBREDDIT_NAME)
    msg_body = "Hello {},\n\nA file storage link was detected at: {}\n\nDoes this require to be backed up?".format(mod_redditor, url)

    mod_redditor.message(msg_subject, msg_body)
    logging.info("Notified moderator: {}".format(constants.MOD_REDDITOR_NAME))

def reply_to_post(text_model):
    author = text_model.author

    message = "Hello {},\n\nA temporary file storage link was detected involving: {}\n\nJust wanted to let you know the file may disappear after a few weeks.".format(author, constants.TEMP_HOSTING_BASE)
    text_model.reply(message)
    logging.info("Replied to post")
