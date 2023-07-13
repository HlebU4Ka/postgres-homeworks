import psycopg2
import csv
import os

with psycopg2.connect(host="localhost",
                        database="postgres-homeworks",
                        user="postgres",
                    password="0052533") as conn:
    # try:
    with conn.cursor() as cur:
            with open(os.path.join('..', 'homework-1', 'north_data', 'customers_data.csv'), 'r',
                      encoding='utf-8') as f:
                # запись данных в переменную
                csv_text = csv.reader(f)
                next(csv_text)
                # запись данных в таблицу
                for i in csv_text:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", tuple(i))

    with open(os.path.join('..', 'homework-1', 'north_data', 'employees_data.csv'), 'r', encoding='utf-8') \
                as file_employees:
            # запись данных в переменную
            csv_text = csv.reader(file_employees)
            # пропуск первой строчки
            next(csv_text)
            # запись данных в таблицу
            for i in csv_text:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', tuple(i))

    with open(os.path.join('..', 'homework-1', 'north_data', 'orders_data.csv'), 'r', encoding='utf-8') \
                as file_order:
            # запись данных в переменную
            csv_text = csv.reader(file_order)
            # пропуск первой строчки
            next(csv_text)
            # запись данных в таблицу
            for i in csv_text:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', tuple(i))

    # except binary.Error as e:
    #     print("Error connecting to the database:", e)

conn.close()
