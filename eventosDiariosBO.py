#!/usr/bin/python3

#import json
#import os
from email.mime.text import MIMEText
from smtplib import SMTP
import time
from datetime import datetime#, timedelta
#import pytz


#from_address = 'alejandra.rodriguez@gmsectec.com'
from_address = 'sumo-alerts@gmsectec.com'
#to_address = ['carlos.lopez@officedepot.com.mx','gmstsa.alertas@officedepot.com.mx','igmorales@officedepot.com.mx','jlgarcia@officedepot.com.mx','jsanchez@officedepot.com.mx','ltorres@officedepot.com.mx','martinezp.cesar@officedepot.com.mx','miguel.aviles@officedepot.com.mx','marcelo.velasco@gmsectec.com','georgie.berrios@gmsectec.com','alejandra.rodriguez@gmsectec.com','brenda.zamora@officedepot.com.mx']
#addressPass = "aLE2143034853"
addressPass = "dQKD7brV7tGZ36Rc"
#to_address = ['marcelo.velasco@gmsectec.com','georgie.berrios@gmsectec.com','alejandra.rodriguez@gmsectec.com']
to_address = ['luis.cano@gmsectec.com']

now = datetime.now()

message = "Persona"
print(message)
print(now.day)



# mime_message = MIMEText (message,'html')
# mime_message['From'] = from_address
# mime_message['To'] = ", ".join(to_address)
# mime_message['Subject'] = 'Prueba'

# smtp = SMTP('smtp.office365.com',587)
# smtp.ehlo()
# smtp.starttls()
# smtp.ehlo()
# smtp.login(from_address,addressPass)
# smtp.sendmail(from_address, to_address, mime_message.as_string())
# smtp.quit()
