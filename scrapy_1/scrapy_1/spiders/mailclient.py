#!/usr/bin/python

import smtplib


def send_email(sender, receivers, message_subject, message_body):
    sender = ('Raspberry Paunov', 'raspberry.paunov@gmail.com', 'Em1l1yan!')
    receivers = (('Emiliyan Paunov', 'emiliyan.paunov@gmail.com'))
    message_subject = 'News for Muziekgebouw Pannenkoen Concerten'
    message_body = "I am the body."
    message = """From: {} {}
To:  {} {}
Subject: {} {}

{}
""".format(sender[0], sender[1], receivers[0][0], receivers[0][1], message_subject, message_body)

    try:
        smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
        smtpObj.starttls()
        smtpObj.login(sender[1], sender[2])
        smtpObj.sendmail(sender, receivers[0][1], message)         
        print "Successfully sent email"
    except smtplib.SMTPException as e:
        print "Error: unable to send email:", e
