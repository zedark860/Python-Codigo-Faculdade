import psycopg2

DB_CONNECTION: psycopg2 = psycopg2.connect(database="BancoExemploAgenda", user="postgres", password="1234", host="localhost", port="5432")

print(DB_CONNECTION.info)

cursor: psycopg2 = DB_CONNECTION.cursor()

cursor.execute('SELECT * FROM public."AGENDA";')

print(cursor.fetchall())