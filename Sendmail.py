import os
import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = ""
EMAIL_PASSWORD = ""

def sendQr(mail:str):
    try :
        msg = EmailMessage()
        msg['Subject'] = 'QR Code of Participation in GDSC Hackday'
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = mail

        msg.set_content('Show the Qr Code to the Organizer')
        with open(f'db/images/{mail}.png','rb') as f:
            imageData = f.read()
            imageType= imghdr.what(f.name)
            imageName = f.name
           
    
        msg.add_alternative(imageData,maintype='image',subtype=imageType,filename=imageName)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
        print(f"Mail Sent To : {mail}")
    except Exception as e :
        print(f"Cannot Send mail to {mail} \n Error : {e}")

