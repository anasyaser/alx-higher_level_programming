#!/usr/bin/python3
"""
Connect python to MySQLdb module and fetch all states match given name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2])
    cur = conn.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}'".format(args[3])

    cur.execute(query)

    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
