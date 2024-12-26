
# FROM python:3.10


# WORKDIR /MatchHub


# COPY . /MatchHub


# RUN pip install --no-cache-dir --upgrade -r /MatchHub/requirements.txt


# CMD ["fastapi", "run", "app.py", "--port", "80"]

FROM python:3.10

WORKDIR /app

COPY . /app

RUN pip install -rU requirements.txt

EXPOSE 50051

CMD ["python", "server.py"]
