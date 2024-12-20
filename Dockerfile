
FROM python:3.10


WORKDIR /MatchHub


COPY ./* /MatchHub


RUN pip install --no-cache-dir --upgrade -r /MatchHub/requirements.txt


CMD ["fastapi", "run", "app.py", "--port", "80"]