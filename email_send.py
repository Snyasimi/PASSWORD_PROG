



import smtplib
from email.message import EmailMessage
#set password and acc to use 

EMAIL_PASSOWRD = "use env variable'
EMAIL_ADRESS = "set env variable"


with smtplib.SMTP_SSL("smtp.gmail.com ,465) as SMTP :
#secures,encrypts a connecton
                      



msg = EmailMessage()
msg["Subject"] = "input txt"
msg["From"] ="input"
                    
msg["to"] = "input'
msg.set_content("string)
               

with smtplib.SMTP_SSL("smtp.gmail.com",465) as smtp:
                #login to your gmail
                smtp.login("*email adress here","*paswd")
                #send email
                smtp.send_message(msg)
