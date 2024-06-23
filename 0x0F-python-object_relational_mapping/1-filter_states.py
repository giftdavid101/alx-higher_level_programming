#!/usr/bin/python3
"""
Python script that lists all states with
a name starting with N (upper N) from the database
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states WHERE name
                      LIKE 'N%' ORDER BY id ASC")
    rows = db_cursor.fetchall()
    for row in rows:
        if row[1][0] == 'N':
            print(row)
