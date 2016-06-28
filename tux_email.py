# tux_email
# Ryan Gavigan
# 06/26/16
import smtplib
from email.mime.text import MIMEText


class tuxEmail:
	'''
	Email the user the RSS title & write event status to database
	'''
	def __init__(self, emailAddress, rssTitle):
		self.emailAddress = emailAddress
		self.rssTitle = rssTitle

	def sendEmail(self, emailAddress, tuxPayload):
		emailAddress = input("Enter the recipient email address: ")
		print emailAddress
		msg = MIMEText('Content of email')
		msg['Subject'] = 'Subject'
		msg['From'] = emailAddress
		msg['To'] = emailAddress
		print "Sending email...."
		print smtplib.SMTP.verify(emailAddress)
		try:
			smtplib.SMTP.connect('smtp.psu.edu')
		except smtplib.SMTPConnectError:
			insertEvent('EO')
		try:
			s.send_messa(msg)
		except smtplib.SMTPException:
			insertEvent("EF")
		s.quit()
		insertEvent("EO")
		print "Email sent!"
