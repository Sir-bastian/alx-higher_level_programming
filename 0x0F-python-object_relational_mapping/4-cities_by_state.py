#!/usr/bin/python3
""" A script that lists all cities
from the Database """


import MySQLdb
import sys
if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute(" SELECT * FROM cities ORDER BY cities.id ASC")
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
