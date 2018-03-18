import psycopg2

connection = psycopg2.connect(database = "demo", user="postgres", password="postgres", host="127.0.0.1", port="5432")

print("connection successfully established");

cur = connection.cursor()

cur.execute("SELECT id, name, address, salary from COMPANY")
rows = cur.fetchall()

for row in rows:
    print("ID =", row[0])
    print("NAME =", row[1])
    print("ADDRESS =", row[2])
    print("SALARY =", row[3])

print("Operation done successfully")

connection.close()
