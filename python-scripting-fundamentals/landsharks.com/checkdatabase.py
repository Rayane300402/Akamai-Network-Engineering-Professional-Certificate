#!/usr/bin/env python3
import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'root',
    database = 'python'
)

cursor = db.cursor()

cursor.execute('SELECT * FROM users')

allUsers = cursor.fetchall()

for i in allUsers:
    print(i)

print("")
input()

cursor.execute('SELECT * FROM customers')

allCustomers = cursor.fetchall()

for i in allCustomers:
    print(i)

print("")
input()


cursor.execute('SELECT * FROM incidents')

allIndicents = cursor.fetchall()

for i in allIndicents:
    print(i)

print("")
input()

cursor.execute('SELECT * FROM employees')

allEmployees = cursor.fetchall()

for i in allEmployees:
    print(i)

print("")
input()

cursor.close()
db.close()












