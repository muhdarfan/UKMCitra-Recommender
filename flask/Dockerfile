FROM python:3.8-slim

# Install pip requirements
#RUN python -m pip install -r requirements.txt

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["gunicorn --bind 0.0.0.0:5000 main:app" ]