import os, time
from datetime import datetime
import smtplib
import numpy as np
email = os.environ.get("EMAIL_ADDRESS")
passw = os.environ.get("EMAIL_PASSWORD")
curl_exp = "curl -s http://checkip.dyndns.org/ | sed 's/[a-zA-Z<>/ :]//g'"
try:
    ip = os.popen(curl_exp).read()
except:
    time.sleep(120)
    ip = os.popen(curl_exp).read()

ip = os.popen(curl_exp).read()

def sendmemyip():
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(email, passw)
        try:
            ip = os.popen(curl_exp).read()
        except:
            time.sleep(120)
            ip = os.popen(curl_exp).read()
        subject = f"my current IP is {ip}"
        current_time = str(datetime.now())
        body = f'this {ip} was at Moscow time: {current_time}'
        msg = f'Subject: {subject}\n\n{body}'
        sender, receiver, message = email, email, msg
        smtp.sendmail(sender, receiver, message)

sendmemyip()
seconds = 1800
for i in np.arange(8760*2): #1 year
    time.sleep(seconds)
    try:
        fresh_ip = os.popen(curl_exp).read()
    except:
        time.sleep(60)
        fresh_ip = os.popen(curl_exp).read()
    if fresh_ip == ip:
        pass
    else:
        sendmemyip()

