#!/usr/bin/python3
"""Connect python to MySQLdb module and write mysql query"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
