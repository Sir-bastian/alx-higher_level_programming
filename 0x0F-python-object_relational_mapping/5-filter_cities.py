#!/usr/bin/python3
"""A script that takes in the name of a state
as an argument, and lists all cities of that
state"""


import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    state_name = sys.argv[4]

    query = f"""SELECT cities.name FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = '{state_name}'
                ORDER BY cities.id ASC"""
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()
