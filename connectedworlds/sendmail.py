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

recipient = "71bjtizui0xpgnne0buv@connectedworlds.dwrensha.ws"
carmen = "carmen@warden.net"

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Re: travel plans'
msg['From'] = '"Carmen" <' + carmen + '>'
msg['To'] = recipient


msg2 = MIMEText(
"""
whoa! that's awesome! Reminds me of Doctor Who: "time can be rewritten"
""")

msg2['Subject'] = 'Re: phone conversation'
msg2['From'] = '"Carmen" <' + carmen + '>'
msg2['To'] = recipient


########################

fp = open('vimeo.txt', 'rb')
vimeomsg = MIMEText(fp.read())
vimeo = "vimeo@email.vimeo.com"
vimeomsg['Subject'] = 'Helena, meet Vimeo'
vimeomsg['From'] = vimeo
vimeomsg['To'] = recipient


fp = open('pinterest.txt', 'rb')
pinterestmsg = MIMEText(fp.read())
pinterest = "pinbot@pinterest.com"
pinterestmsg['Subject'] = 'Welcome to Pinterest'
pinterestmsg['From'] = pinterest
pinterestmsg['To'] = recipient

#######

spam1 = MIMEText(
"""
http://www.gutenberg.org/files/38193/38193-h/38193-h.htm#Apple_Cake
and http://upload.wikimedia.org/wikipedia/commons/4/44/Birthday_Cake-_Virginia.jpg
""")

spam1["Subject"]  = "h0tt fresh c4ke"
spam1["From"] = "abcde@bakery.com"
spam1["To"] = recipient

spam2 = MIMEText(
"""
learn history accredited courses now
http://www.shorehamvillage.org/Shoreham_History/History_home.html
"""
)
spam2["Subject"]  = "LEARN HISTORY"
spam2["From"] = "prof@tenure.biz"
spam2["To"] = recipient



spam3 = MIMEText(
"""
cheap fast academic papers
contact Rob Simmons guaranteed new paper can't be caught by pl4giarism detector
"""
)
spam3["Subject"]  = "impress her t0night"
spam3["From"] = "rob@academy.edu"
spam3["To"] = recipient


spam4 = MIMEText(
"""
h4x0r
David Renshaw
"""
)
spam4["Subject"]  = "MAKING IT POSSIBLE"
spam4["From"] = "david@dwrensha.ws"
spam4["To"] = recipient


spam5 = MIMEText(
"""
grandma impression from kind internet stranger

Scooter Burch
"""
)

spam5["Subject"]  = "HELP 4 U"
spam5["From"] = "ths@inter.net"
spam5["To"] = recipient

s = smtplib.SMTP('localhost', 30025)
#s.sendmail(carmen, [recipient], msg.as_string())
#s.sendmail(carmen, [recipient], msg2.as_string())
#s.sendmail(vimeo, [recipient], vimeomsg.as_string())
#s.sendmail(pinterest, [recipient], pinterestmsg.as_string())
#s.sendmail(spam1["From"], [recipient], spam1.as_string())
#s.sendmail(spam2["From"], [recipient], spam2.as_string())
#s.sendmail(spam3["From"], [recipient], spam3.as_string())
#s.sendmail(spam4["From"], [recipient], spam4.as_string())
s.sendmail(spam5["From"], [recipient], spam5.as_string())


s.quit()


