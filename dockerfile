FROM python:3.8-slim

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
RUN openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365

COPY . .

ENTRYPOINT [ "python" ]
CMD ["api.py" ]
