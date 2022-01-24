FROM python:3.8-slim

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . /app
WORKDIR /app

#RUN apt-get clean && apt-get -y update
#RUN 

ENTRYPOINT [ "python" ]

CMD ["api.py" ]
