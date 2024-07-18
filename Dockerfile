FROM docker.io/library/python:latest

RUN pip install psycopg2
COPY rds.py /
CMD [ "python", "/rds.py" ]
