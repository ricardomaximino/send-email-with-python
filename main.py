import smtplib
import pandas
from datetime import datetime
from random import choice, randint

now = datetime.now()
today_tuple = (now.month, now.day)


def get_random_quote():
    quote = ""
    with open("resources/quotes.txt") as quote_file:
        quotes = quote_file.readlines()
        quote = choice(quotes)

    return quote


def send_email(email, password, emails, subject, message, smtp="smtp.gmail.com"):
    with smtplib.SMTP(smtp) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=emails,
            msg=f"Subject:{subject}\n\n{message}")


def react_to_birthday():
    data = pandas.read_csv("resources/birthdays.csv")
    birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
    while today_tuple in birthdays_dict:
        birthdays_person = birthdays_dict.pop(today_tuple)
        file_path = f"resources/letter_{randint(1,3)}.text"
        with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", birthdays_person["name"])
            content = content.replace("[QUOTE]", get_random_quote())
            send_email(
                "brasajava@gmail.com",
                "SantaPola2020",
                "ricardomaximino@gmail.com",
                "Dally Motivation Phrase",
                content
            )


def dally_motivation_phrase():
    send_email(
        "brasajava@gmail.com",
        "BrasaJava2014",
        "ricardomaximino@gmail.com",
        "Dally Motivation Phrase",
        get_random_quote()
    )


react_to_birthday()
dally_motivation_phrase()
