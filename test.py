import smtplib
import os
print(os.environ.get('EMAIL_USER'))
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#print(EMAIL_ADDRESS, EMAIL_PASSWORD)
#with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    
server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)

server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

subject = 'Sample Email'
body = 'This is a test email'
msg = f'Subject: {subject}\n\n{body}'

server.sendmail(EMAIL_ADDRESS, 'aidelrea@asu.edu', msg)