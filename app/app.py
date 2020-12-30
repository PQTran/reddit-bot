import constants
import helper
import reddit_helper
import submissions
import comments
import sys

def main(target_content):
    helper.configure_logging(target_content)
    reddit = reddit_helper.get_reddit_instance()
    subreddit = reddit_helper.get_subreddit(constants.SUBREDDIT_NAME)
    if target_content == "submissions":
        submissions.stream_submissions(subreddit)
    elif target_content == "comments":
        comments.stream_comments(subreddit)
    else:
        raise ValueError("invalid stream content argument")

main(sys.argv[1])
