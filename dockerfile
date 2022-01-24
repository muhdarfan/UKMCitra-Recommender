FROM ubuntu:18.04
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential

#FROM python:3.8-slim


COPY . /app
WORKDIR /app

# Install pip requirements
#COPY requirements.txt .
RUN python -m pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD ["api.py" ]
