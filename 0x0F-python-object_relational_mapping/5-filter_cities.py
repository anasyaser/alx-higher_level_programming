#!/usr/bin/python3
"""
Connect python to MySQLdb module and fetch all states match given name
BUT make sure to be safe from  sql injection attacks
"""
import MySQLdb
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=args[0],
                           passwd=args[1], db=args[2])
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name FROM states INNER JOIN cities\
    ON states.id = cities.state_id WHERE states.name = %s ORDER BY cities.id",
                [args[3]])

    query_rows = cur.fetchall()

    for row in query_rows:
        if (row == query_rows[-1]):
            print(row[1], end='')
        else:
            print(row[1], end=", ")
    print()
    cur.close()
    conn.close()
