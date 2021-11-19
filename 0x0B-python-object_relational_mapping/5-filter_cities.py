#!/usr/bin/python3
"""Lists given city from database"""


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
        "SELECT cities.name, states.name FROM cities\
	 INNER JOIN states ON cities.state_id = states.id\
	 ORDER BY cities.id ASC")
    cts = cur.fetchall()
    for i, ct in enumerate(cts, start=0):
        if i != 0:
            print(", ", end="")
        print(ct[0], end="")
    print("")
    cur.close()
    DB.close()
