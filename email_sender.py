# nano .bash_profile

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "143shyamu@gmail.com"
toaddr = "shyamu.anugandula@vertoz.com"
password = os.environ.get('email_password')
print(password)
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python email"
body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('pop.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login("143shyamu@gmail.com", "saroja143")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)