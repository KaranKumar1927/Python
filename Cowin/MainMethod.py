# import the smtplib module. It should be included in Python by default
import smtplib
# import necessary packages
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ReadContacts import *

# import smtplib, ssl
# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "mailnow4akash@gmail.com"  # Enter your address
# receiver_email = "karan1198kumar@gmail.com"  # Enter receiver address
# password = input("Type your password and press enter: ")
# message = """\
# Subject: Hi there
# This message is sent from Python."""
# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
# set up the SMTP server

smtpObj = smtplib.SMTP(host='smtp.gmail.com', port=587)
smtpObj.starttls()
smtpObj.login('mailnow4akash@gmail.com','Akash1234#')
contactList = 'C:/PythonPracs/Cowin/mailId.txt'
template = 'C:/PythonPracs/Cowin/messageTemplate.txt'
names, emails = get_contacts(contactList)  # read contacts
message_template = read_template(template)

# For each contact, send the email:

def sendMail():
    for name, email in zip(names, emails):
        msg = MIMEMultipart()       # create a message

        # add in the actual person name to the message template
        message = message_template.substitute(PERSON_NAME=name.title())

        # setup the parameters of the message
        msg['From']='mailnow4akash@gmail.com'
        msg['To']='pavansatish237@gmail.com'
        msg['Subject']="Vaccine Availability "

        # add in the message body
        msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier.
        smtpObj.send_message(msg)
        
        del msg



