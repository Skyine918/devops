FROM python:3.8-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies required for psycopg2 python package
#RUN apk update && apk add libpq
#RUN apk update && apk add python3-dev gcc build-base musl-dev postgresql-dev libffi-dev gcc libc-dev jpeg-dev zlib-dev

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

WORKDIR /usr/src/app/app_python
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]