FROM tiangolo/uwsgi-nginx-flask:python3.10

ENV LISTEN_PORT 8080
EXPOSE 8080

COPY ./app /app