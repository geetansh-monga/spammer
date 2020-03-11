import smtplib
from email.message import EmailMessage 


print('Setup...')
count = 0
server = smtplib.SMTP('smtp.gmail.com', 535 )
server.ehlo()
server.starttls()
server.ehlo()
server.login('xyz@gmail.com', 'password')

data = ['pheonix4374@gmail.com']

for email in data: 
    msg = EmailMessage()
    msg['Subject'] = 'Confirmation/RSVP for the MLH localhost'
    msg['From'] = '<from email>' 
    msg['To'] = f"{email}"
    msg.set_content('Hey Hemu', subtype = 'html')

    server.send_message(msg)
    print('sent')
    count = count + 1

print(count)
