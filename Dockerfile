FROM python:3.8.2
ENV PYTHONUNBUFFERED 1
RUN apt-get update -qq && apt-get install -yq \
  exuberant-ctags \
  netcat \
  postgresql-client
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN SECRET_KEY=unset python manage.py collectstatic --no-input
ENV WEB_CONCURRENCY 3
ENV WORKER_CONNECTIONS 50
ENV PORT 8000
CMD gunicorn stopcovid.wsgi -k gevent --worker-connections $WORKER_CONNECTIONS --bind 0.0.0.0:$PORT --config gunicorn_config.py --max-requests 10000 --max-requests-jitter 1000 --access-logfile -
