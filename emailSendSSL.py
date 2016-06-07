#!/usr/bin/python
# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Setup the email components Subject, From, To
fromAddress = 'jxo19@psu.edu'
toAddress = 'jxo19@psu.edu'
subject = 'subject line of email'

msg = MIMEText('Content of email')
msg['Subject'] = 'Subject'
msg['From'] = fromAddress
msg['To'] = toAddress

# Send the message via the SMTP server
try:
   s = smtplib.SMTP_SSL('authsmtp.psu.edu, 465)
   s.sendmail(fromAddress, [toAddress], msg.as_string())
except Exception as e:
   print "Error %s" % e.args[0]
finally:
   s.quit()


