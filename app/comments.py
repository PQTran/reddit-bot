import helper
import logging
import reddit_helper

def process_comment(comment):
    logging.info("Started to process comment: (id={}, submission_id={})".format(comment.id, comment.link_id))
    helper.process_temp_storage(comment.body, comment)
    helper.process_main_storage(comment.body, comment.permalink)
    logging.info("Finished processing comment: (id={}, submission_id={})".format(comment.id, comment.link_id))

def stream_comments(subreddit):
    for comment in subreddit.stream.comments(skip_existing=True):
        if comment.author != reddit_helper.get_bot_redditor():
            process_comment(comment)
