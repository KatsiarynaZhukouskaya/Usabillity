from peewee import *
from models import db
from garden import month
from openpyxl import open


garden_advice = open("garden.xlsx", read_only=True)

with db:
    db.create_tables(month)
   
    for i in range(len(garden_advice.worksheets)):
        sheet = garden_advice.worksheets[i]
        garden = []
        for row in range (2, sheet.max_row+1):
            name = sheet[row][1].value
            description = sheet[row][2].value
            garden.append({"name": name, "description": description})

        advice = month[i].insert_many(garden).execute()


