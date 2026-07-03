import smtplib

my_email = "nadikapriya2210@gmail.com"
password = "smyfzcpwrcgjsggs"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#   connection.starttls() 
#   connection.login(user=my_email, password=password)
#   connection.sendmail(
#     from_addr=my_email, 
#     to_addrs="nadikapriya2210@gmail.com", 
#     msg="Subject:Hello this is a test email from Python\n\nHello, this is a test email from Python")

import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
  with open("quotes.txt", "r") as file:
    quotes = file.readlines()
    quote = random.choice(quotes)
  
  print(quote)
  with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
      from_addr=my_email,
      to_addrs="nadikapriya2210@gmail.com",
      msg=f"Subject:Quote of the Day\n\n{quote}")