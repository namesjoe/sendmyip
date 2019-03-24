import os
from datetime import datetime
import smtplib

email = os.environ.get("EMAIL_ADDRESS")
passw = os.environ.get("EMAIL_PASSWORD")
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(email, passw)
    ip = os.popen("curl -s http://checkip.dyndns.org/ | sed 's/[a-zA-Z<>/ :]//g'").read()
    subject = f"my current IP is {ip}"
    current_time = str(datetime.now())
    body = f'this {ip} was at Moscow time: {current_time}'
    msg = f'Subject: {subject}\n\n{body}'
    sender, receiver, message = email, email, msg
    smtp.sendmail(sender, receiver, message)


