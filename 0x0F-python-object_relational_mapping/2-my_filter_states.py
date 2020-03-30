#!/usr/bin/python3
'''
Lists all states in a table that matches argv[4]
'''
if __name__ == "__main__":
    import sys
    import MySQLdb
    
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name='{}'".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print((state))
