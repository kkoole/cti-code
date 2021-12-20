#!/usr/bin/env python3

'''
GetDatabaseInfoTest.py: Python script for Wk6 CTI assignment 2 Python output.
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mysql.connector

SMTP_SERVER = 'smtp.gmail.com'
SMTP_SSLPORT = 465
SMTP_USERNAME = 'someone@example.com'
SMTP_PASSWORD = 'supersecret'

FROM_ADDRESS = 'someone@example.com'

MYSQL_HOST = 'localhost'
MYSQL_USER = 'username'
MYSQL_PASSWORD = 'supersecret'


def SendGmail(toAddress, subject, body):
    msg = MIMEMultipart()
    msg['From'] = FROM_ADDRESS
    msg['To'] = toAddress
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_SSLPORT)
    server.login(SMTP_USERNAME, SMTP_PASSWORD)
    text = msg.as_string()
    server.sendmail(FROM_ADDRESS, toAddress, text)


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

    toAddress = 'someone@example.com'
    subject = "dnsinfo report"
    body = "Hello\n\nThis is a report for SQL query: {}\nThe result of this query is: {}\n\nRegards,\nYour Friendly CTI ;)".format(query, result)

    SendGmail(toAddress, subject, body)


if __name__ == '__main__':
    main()
