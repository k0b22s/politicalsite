
FROM python:3.8-slim-buster
WORKDIR /app
COPY Campaigning/requirements.txt /app
Run pip install --trusted-host pypi.python.org -r requirements.txt
COPY Campaigning /app
EXPOSE 8000
ENV PYTHONBUFFERED 1
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
