#!/usr/bin/env python3
# Lists all of the states in the table
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
