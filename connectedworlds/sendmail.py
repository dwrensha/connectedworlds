#! /usr/bin/python
import sys;

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# sendmail filename from to
#if len(sys.argv) != 4:
#    print "usage: ./sendmail.py filename from to"
#    exit(1)



# Create a text/plain message
msg = MIMEText(
"""
haha I might be in Hawaii too! John and I were thinking of starting with San Diego (get it?) for the hmoon but probably gonna go some other places too.  Let me know if you have time to meet up.
"""
)

recipient = "hgrx3qavoeh8s6vzeaq5@connectedworlds.dwrensha.ws";
carmen = "carmen@example.com"


# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Re: travel'
msg['From'] = '"Carmen San Diego" <' + carmen + '>'
msg['To'] = recipient

########################

fp = open('vimeo.txt', 'rb')
vimeomsg = MIMEText(fp.read(), 'html')
vimeo = "vimeo@email.vimeo.com"
vimeomsg['Subject'] = 'Helena, meet Vimeo !!'
vimeomsg['Date'] = 'Sun, Aug 24, 2014 at 12:10 PM'
vimeomsg['From'] = vimeo
vimeomsg['To'] = recipient



s = smtplib.SMTP('localhost', 30025)
#s.sendmail(carmen, [recipient], msg.as_string())
s.sendmail(vimeo, [recipient], vimeomsg.as_string())
s.quit()


