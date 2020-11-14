import csv
import sys
from cs50 import SQL

if len(sys.argv) != 2:
    print("Usage ./python import.py <nameofthecsvfile>")
db = SQL("sqlite:///students.db")

with open(sys.argv[1], newline='') as f:
    reader = csv.DictReader(f)

    for i in reader:
        if len(i["name"].split()) == int(2):
            firstname = i["name"].split()[0]
            lastname = i["name"].split()[1]
            house = i["house"]
            birth = i["birth"]
            middle = None
            db.execute("INSERT INTO students (first,middle,last,house,birth) VALUES (?,?,?,?,?)",firstname,middle,lastname,house,birth)
        else:
            firstname = i["name"].split()[0]
            middlename = i["name"].split()[1]
            lastname = i["name"].split()[2]
            house = i["house"]
            birth = i["birth"]
            db.execute("INSERT INTO students (first,middle,last,house,birth) VALUES (?,?,?,?,?)",firstname,middlename,lastname,house,birth)
