# tux_master
# Ryan Gavigan
# 06/20/16

import tux_regexp
import tux_database
import tux_email
import tux_rss
import tux_oop
import subprocess

subprocess.call('clear', shell=True)

tuxpay1 = tux_regexp.UserInput()

print "feed: " + tuxPay1.rssFeed
print "address: " + tuxPay1.emailAddress
print "date: " + tuxPay1.date

# Order of processes:
# Process1:(tux_regexp.py) accept user input and populate the tux entity and
    # write the event status to the database.
# Process2:(tux_rss.py) try and get the RSS feed & write event status to db
# Process3:(tux_email.py) email user the RSS title & write event status to db.
# Process4: read the database status events and print them out to the screen.
