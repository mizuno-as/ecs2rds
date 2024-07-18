import psycopg2
import os

Database_endpoint = os.environ['ENDPOINT']
Username = os.environ['USER']
Password = os.environ['PASS']
Port = os.environ['PORT']
Database = os.environ['DATABASE']

try:
  print(f'Connecting to {Username}@{Database_endpoint}/{Database}:{Port}')
  db = psycopg2.connect(f'host={Database_endpoint} port={Port} dbname={Database} user={Username} password={Password}')
  db.get_backend_pid()
  print(f'Connection successful to {Username}@{Database_endpoint}/{Database}:{Port}')
  db.close()
except Exception as e:
  print("Connection unsuccessful due to " + str(e))

