FROM python:3.9
WORKDIR /app
RUN pip install praw url_regex
RUN apt-get update && apt-get install -y npm && npm install -g nodemon
