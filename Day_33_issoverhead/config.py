import smtplib

my_mail = "pavani9419@gmail.com"
my_password = "wwhw jyxe hoxx tpwn"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_mail, password=my_password)
    connection.sendmail(
        from_addr=my_mail, 
        to_addrs="pavanigudupu12523@gmail.com",
        msg="Subject: Isso\n\nThis is the body"
    )