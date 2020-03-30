#!/usr/bin/python3
# This script lists all cities
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name \
                FROM cities \
                LEFT JOIN states \
                ON cities.state_id=states.id \
                ORDER BY cities.id")
    states = cur.fetchall()
    for state in states:
        print(state)
