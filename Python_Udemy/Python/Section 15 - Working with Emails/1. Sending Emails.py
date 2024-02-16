# ---------------------------------------------------------------------------- #
#                                Sending Emails                                #
# ---------------------------------------------------------------------------- #

import smtplib
import getpass

# Creating smtp object
smtp_object = smtplib.SMTP('smtp.gmail.com' , 587)

# Establishing connection to server
smtp_object.ehlo()

smtp_object.starttls()

# Setting up email and password and login
# Getpass will hide password entry
password = getpass.getpass('What is your password: ')
email = getpass.getpass('Email: ')

smtp_object.login(email, password)

# Sending email
from_address = email
to_address = email
subject = input("Subject line: ")
message = input("Body message: ")
msg = "Subject: " + subject + "\n" + message

smtp_object.sendmail(from_address,to_address, msg)

# Now it is sent, quit the connection
smtp_object.quit()




