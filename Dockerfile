FROM python:3.6.2-slim
MAINTAINER Jonathan Querubina <john@d3.do>

RUN apt-get update && apt-get install -qq -y \
  build-essential libpq-dev libffi-dev --no-install-recommends

EXPOSE 8000
RUN mkdir /app
WORKDIR /app

ADD requirements.txt /app

RUN pip install -r requirements.txt

ADD . /app
CMD /app/manage.py runserver 0.0.0.0:8000
