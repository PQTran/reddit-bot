import constants
import reddit_helper

from pathlib import Path
import logging
import url_regex

LOG_DIRECTORY = "../log"

def matches_domain_base(domain, base_list):
    for domain_base in base_list:
        if domain.find(domain_base) != -1:
            return True
    return False

def process_temp_storage(text, text_model):
    links = url_regex.UrlRegex(text).links
    temp_storage_links = list(filter(lambda url : matches_domain_base(url.domain, constants.TEMP_HOSTING_BASE), links))
    if len(temp_storage_links) > 0:
        reddit_helper.reply_to_post(text_model)

def process_main_storage(text, source_url):
    links = url_regex.UrlRegex(text).links
    sourcelinks = list(filter(lambda url : matches_domain_base(url.domain, constants.FILE_HOSTING_BASE), links))
    if len(sourcelinks) > 0:
        reddit_helper.notify_moderator(source_url)

def configure_logging(target_content):
    log_path = Path(LOG_DIRECTORY)
    log_path.mkdir(exist_ok=True)
    logging.basicConfig(format="%(asctime)s %(message)s", filename="../log/{}-output.log".format(target_content), level=logging.INFO)
