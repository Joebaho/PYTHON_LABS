'''
AWS CODE: rds_connect.py

Write a program that will connect to an RDS (MySQL or PostgreSQL) instance, you will need libraries like pymysql or psycopg2.
'''

import pymysql

connection = pymysql.connect(
    host='your-rds-endpoint',
    user='your-username',
    password='your-password',
    database='your-database'
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM your_table")

for row in cursor.fetchall():
    print(row)

connection.close()
