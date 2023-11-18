#!/usr/bin/python3

""" A script that lists all states
from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == '__main__':
    my_username = sys.argv[1]
    my_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port="3306",
            user="my_username",
            passwd="my_password",
            database="database_name"
            )

    cur = db.cursor()
    """ getting a cursor """

    cur.excute("SELECT * FROM states ORDER BY id ASC")
    """excute the SQL query to retrieve all the states and sort them
    states.id in Ascending order"""

    rows = cur.fetchall()
    """ Get all the rows returned by the query"""

    """ Display all the rows returned by the query """
    for state in states:
        print(state)

    """ close the cursor and the connection """
    cur.close()
    db.close()
