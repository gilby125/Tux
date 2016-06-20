# tux_email
# Ryan Gavigan
# 06/20/16
import smtplib
from email.mime.text import MIMEText



class tuxEmail:
    '''
    Email the user the RSS title & write event status to database
    '''
    def __init__(self, emailAddress, rssTitle):
        self.emailAddress = emailAddress
        self.rssTitle = rssTitle

    def sendEmail(self, emailAddress):
        emailAddress = input("Enter the recipient email address:\t")
        print(emailAddress)
        s = smtplib.SMTP('smtp.psu.edu')
        msg = MIMEText('Content of email')
        msg['Subject'] = 'Subject'
        msg['From'] = emailAddress
        msg['To'] = emailAddress
        print("Sending email....")
        s.sendmail(emailAddress, emailAddress, msg.as_string())
        s.quit()
