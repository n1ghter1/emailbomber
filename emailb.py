import smtplib
import getpass


user = input("Gmail User: ")
passw = getpass.getpass("Password: ")
recvr = input("Receiving address: ")
msg = input("Message: ")
times = int(input("Number of messages: "))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(user, passw)
for i in range(0, times):
  server.sendmail(user, recvr, msg)
  print ("Sent ")
  server.quit()
else:
    print("Error. ")
    server.quit()
