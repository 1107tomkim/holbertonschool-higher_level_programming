#!/usr/bin/python3
"""Displays all val in staets table where name matches arg"""


from sys import argv
import MySQLdb

if __name__ = "__main__":
    user = argv[1]
    password = argv[2]
    database = argv[3]
    compare = argv[4]

    DB = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database, port=3306)

    cur = DB.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name\
         LIKE '{}' ORDER BY states.id ASC".format(compare))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    DB.close()
