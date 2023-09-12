import smtplib as sl

obj = sl.SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()
obj.login('suraj.sg793@gmail.com', '')
subject = "test python"
body = '''Of course! I can help you with Python. What would you like to know
 or test in Python? Please provide more details or specify your question, and I'll do my best to assist you.'''
massage = "subject : {}\n\n{}".format(subject,body)
listadd = ['suraj.sg8601@gmail.com','suraj.sg3101@gmail.com']
obj.sendmail('suraj.sg793@gmail.com', listadd, massage)
print("mail sended...")
obj.quit()

