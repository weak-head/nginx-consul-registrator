FROM python:3.7-alpine

COPY . /app
WORKDIR /app

RUN pip install Flask requests

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]