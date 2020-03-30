#!/usr/bin/python3
"""
Script that displays all values in the states
table where name matches the argument
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name = %s", (argv[4], ))
    states = cur.fetchall()
    for state in states:
        print(state)
