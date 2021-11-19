#!/usr/bin/python3
"""Lists all cities from the database"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    DB = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database, port=3306)\

    cur = DB.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities, states\
                WHERE states.id = state_id\
                ORDER BY id ASC")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    DB.close()
