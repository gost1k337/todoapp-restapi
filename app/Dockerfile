FROM python:3.8

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install pipenv
COPY Pipfile* /usr/src/app/
RUN pipenv lock --requirements > requirements.txt

RUN pip install -r /usr/src/app/requirements.txt

COPY . /usr/srs/app/

CMD ["pipenv", "run", "flask", "run", "--host", "0.0.0.0", "--port", "$APP_PORT"]
