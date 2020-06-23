import smtplib

sender_email = 'mail_id'
receiver = 'mail_id'
password = 'Gmail Password'
message = "The Website is not running properly."
server =smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,password)
server.sendmail(sender_email,receiver,message)
print("Email has been sent to ", receiver)
