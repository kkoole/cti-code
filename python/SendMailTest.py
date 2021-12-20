#!/usr/bin/env python3

'''
SendMailTest.py: Python script for Wk6 CTI assignment 2 Python output.
'''

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = 'smtp.gmail.com'
SMTP_SSLPORT = 465
SMTP_USERNAME = 'someone@example.com'
SMTP_PASSWORD = 'supersecret'

FROM_ADDRESS = 'someone@example.com'


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


def main():
    toAddress = 'someone@example.com'
    subject = "Test"
    body = "This is a test sending email through python\nRegards"

    SendGmail(toAddress, subject, body)
    

if __name__ == '__main__':
    main()
