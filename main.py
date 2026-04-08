# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.
import os
import smtplib
import datetime as dt
from random import randint
import pandas as pd

MY_EMAIL = os.environ["MY_EMAIL"]
MY_PASSWORD = os.environ["MY_PASSWORD"]


data = pd.read_csv('birthdays.csv')
now = dt.datetime.now()

# Check if today matches a birthday in the birthdays.csv
for row in data.to_dict(orient='records'):

    if now.month == row["month"] and now.day == row["day"]:
        #pick a random letter from templates and replace the [NAME] with the person's actual name from birthdays.csv
        number = randint(1, 3)
        with open(f"letter_templates/letter_{number}.txt", "r") as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", row["name"])

        #send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday\n\n{contents}"
            )




