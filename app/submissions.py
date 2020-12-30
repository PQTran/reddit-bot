import helper
import logging

def process_submission(submission):
    text = submission.selftext if submission.selftext != "" else submission.url
    logging.info("Started to process submission: (id={})".format(submission.id))
    helper.process_temp_storage(text, submission)
    helper.process_main_storage(text, submission.permalink)
    logging.info("Finished processing submission: (id={})".format(submission.id))

def stream_submissions(subreddit):
    for submission in subreddit.stream.submissions(skip_existing=True):
        process_submission(submission)
