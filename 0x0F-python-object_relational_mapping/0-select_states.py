#!/usr/bin/python3

""" A script that lists all states
from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == '__main__':

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            database=sys.argv[3]
            )

    cur = db.cursor()
    cur.excute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    """ Display all the rows returned by the query """
    for state in states:
        print(state)

    """ close the cursor and the connection """
    cur.close()
    db.close()
