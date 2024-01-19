#  sending mail by python (single or multiple person)

import smtplib as s

ob=s.SMTP('smtp.gmail.com',587)
ob.ehlo()
ob.starttls()

ob.login('your email','password')
subject="running program"
body="i am cooder"
message="subject:{}\n\n{}".format(subject,body)
listmail=['mail which you want to send message']

ob.sendmail('your mail',listmail,message)
print("mailsend") 
ob.quit()