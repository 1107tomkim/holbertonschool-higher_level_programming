#!/usr/bin/python3
"""Lists all states from database"""


from sys import argv
import MySQLdb

if __name__ == "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]

    DB = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database, port=3306)

    cur = DB.cursor()

    cur.execute(
	"SELECT * FROM states WHERE name = %(name)s\
        ORDER BY states.id ASC", {'name': argv[4]})
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    DB.close()
