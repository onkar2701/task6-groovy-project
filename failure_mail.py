import smtplib

sender_email = 'onkarkadam27@gmail.com'
receiver = 'sumitpol1995@gmail.com'
password = 'Onkarkadam@2027'
message = "The Website is not running properly."
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,receiver,message)
print("Email has been sent to ", receiver)