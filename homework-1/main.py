import psycopg2
import csv
import os

with psycopg2.connect(host="localhost",
                      database="postgres-homeworks",
                      user="postgres",
                      password="0052533") as conn:
    try:
        with conn.cursor() as cur:
            with open(os.path.join('..', 'homework-1', 'postgres-homeworks', 'customers_data.csv'), 'r',
                      encoding='utf-8') as f:
                csv_text = csv.reader(f)
                next(csv_text)
                for i in csv_text:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(i))
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
