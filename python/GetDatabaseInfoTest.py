#!/usr/bin/env python3

'''
GetDatabaseInfoTest.py: Python script for Wk6 CTI assignment 2 Python output.
'''

import mysql.connector

MYSQL_HOST = 'localhost'
MYSQL_USER = 'username'
MYSQL_PASSWORD = 'supersecret'


def GetDatabaseInfo(sqlQuery):
    # setup db connection
    db = mysql.connector.connect(
        host = MYSQL_HOST,
        user = MYSQL_USER,
        password = MYSQL_PASSWORD
    )
    
    cursor = db.cursor()
    cursor.execute(sqlQuery)
    result = cursor.fetchall()

    return result[0][0]


def main():
    query = 'SELECT IPaddress FROM info.dnsinfo ORDER BY DestinationCount DESC LIMIT 1;'
    result = GetDatabaseInfo(query)
    print('Query result is: ' + result)


if __name__ == '__main__':
    main()
