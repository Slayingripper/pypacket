import smtplib

sender = 'kirav96@gmail.com'
receivers = ['kirav96@gmail.com']

message = """From: From Person <kirav96@gmail.com>
To: To Person <kirav96@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)         
   print ("Successfully sent email")
except SMTPException:
   print ("Error: unable to send email")