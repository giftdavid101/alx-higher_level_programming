#!/usr/bin/python3
"""
Python script that
takes in arguments and displays
all values in the states table of
`hbtn_0e_0_usa`.
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db_connect = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")

    db_cursor = db_connect.cursor()
    db_cursor.execute("SELECT * FROM states \
                       WHERE name LIKE BINARY %(name)s \
                       ORDER BY states.id", (argv[4]))
    rows = db_cursor.fetchall()

    for row in rows:
        print(row)
