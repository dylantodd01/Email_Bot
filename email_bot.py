import smtplib, ssl

port = 465

sender, password = "dylan.pythonbot@gmail.com", "pythonbot"
reciever = "dylantodd00@gmail.com"

message = """\
Subject: The Dylan Bot Is Contacting You

Hello,

This is from Python.

All the best,
DylanBot
"""

context = ssl.create_default_context()

print("Sending mail...")

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
	server.login(sender, password)
	server.sendmail(sender, reciever, message)

print("Sent mail!")