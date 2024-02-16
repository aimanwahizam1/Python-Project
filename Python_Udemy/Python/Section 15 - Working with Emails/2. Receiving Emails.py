# ---------------------------------------------------------------------------- #
#                               Receiving Emails                               #
# ---------------------------------------------------------------------------- #

import imaplib
import getpass
import email

M = imaplib.IMAP4_SSL('imap.gmail.com')

# Email, password and login
email = getpass.getpass('Email: ')
password = getpass.getpass('Password: ')

M.login(email, password)

# Get email directory
print(M.list())

# Go to inbox
M.select('inbox')

# Search for mail
typ, data = M.search(None, 'SUBJECT "test"')

# Now fetch email from data
email_id = data[0]

result, email_data = M.fetch(email_id, '(RFC822)')

# Might have multiple email results, so just pick the first one
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')

email_message = email.message_from_string(raw_email_string)

for part in email_message.walk():
    if part.get_content_type() == 'text/plain':
        body = part.get_payload(decode=True)
        print(body)
