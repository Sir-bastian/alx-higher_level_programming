#!/usr/bin/python3
"""
0-select_states module
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3]
                         searched_name=sys.argv[4])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name
                = '%s' ORDER BY id ASC""", %(searched_name))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
