#!/usr/bin/python3

""" 2-my_filter_states.py module """


import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQL.connect("""host='localhost', port=3306,
                    user=sys.argv[1], passwd=sys.argv[2],
                    db=sys.argv[3]""")

    cursor = db.cursor()
    cursor.execute(""" SELECT * FROM states WHERE name LIKE BINARY
                '{}' BY ORDER states.id ASC""".format(sys.argv[4]))

    rows = cursor.fetchall()
    for state in rows:
        print(state)

    cursor.close()
    db.close()
