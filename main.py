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


def send_email(email, password, emails, subject, message, smtp="smtp.gmail.com", port=587):
    with smtplib.SMTP(smtp, port) as connection:
        connection.starttls()
        connection.login(email, password)
        connection.sendmail(
            from_addr=email,
            to_addrs=emails,
            msg=f"Subject:{subject}\n\n{message}")

# Deprecated because it does not support repeted birthday
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
                "Happy Birthday",
                content
            )


def dally_motivation_phrase(email):
    send_email(
        "brasajava@gmail.com",
        "SantaPola2020",
        email,
        "Dally Motivation Phrase",
        get_random_quote()
    )


def read_birthda_data():
    data = pandas.read_csv("resources/birthdays.csv")
    my_dict = {}

    for data_row in data.itertuples():
        key = (data_row.month, data_row.day)
        if key in my_dict:
            my_dict.get(key).append(data_row)
        else:
            my_dict[key] = [data_row]
    return my_dict


def get_birthday_list(date):
    list = []
    my_dict = read_birthda_data()
    key = (date.month, date.day)
    if key in my_dict:
        list = my_dict[key]
    return list


def send_happy_birth_email():        
    for item in get_birthday_list(datetime.now()):
        file_path = f"resources/letter_{randint(1,3)}.text"
        with open(file_path) as letter_file:
            content = letter_file.read()
            content = content.replace("[NAME]", item.name)
            content = content.replace("[QUOTE]", get_random_quote())
            send_email(
                "brasajava@gmail.com",
                "SantaPola2020",
                item.email,
                "Happy Birthday",
                content
            )

# react_to_birthday()
dally_motivation_phrase(["ricardomaximino@hotmail.com", "ricardomaximino@gmail.com"])
send_happy_birth_email()
