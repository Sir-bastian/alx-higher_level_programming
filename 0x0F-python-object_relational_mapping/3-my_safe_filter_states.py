#!/usr/bin/python3

""" A script that takes in arguments
and displays all values in the table hbtn_0e_0_usa
name matches the argument. But this time,
one that is safe from MySQL injections! """


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cursor = db.cursor()

    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name = %s ORDER BY state.id ASC"
    cursor.execute(query, (state_name,))

    results = cursor.fetchall
    for state in results:
        print(state)

    cursor.close()
    db.close()
