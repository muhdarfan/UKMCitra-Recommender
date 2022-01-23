FROM python:3.8-slim

# Install pip requirements
COPY requirements.txt .
RUN python -m pip install -r requirements.txt

COPY . .

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
