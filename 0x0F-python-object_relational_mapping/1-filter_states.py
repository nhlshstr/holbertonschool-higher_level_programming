#!/usr/bin/python3
#Lists all states in a table that start with 'N'

if __name__ == "__main__":
    import sys
    import MySQLdb
    
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id")
    states = cur.fetchall()
    for state in states:
        if (state[1][0] == "N"):
            print((state))
