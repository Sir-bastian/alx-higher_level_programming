#!/usr/bin/python3
"""A script that takes in the name of a state
as an argument, and lists all cities of that
state"""


import MySQKdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host=localhost, port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    arg = sys.argv[4]

    query =  """SELECT cities.name FROM states WHERE name = %s
                ORDER BY cities.id ASC"""
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
