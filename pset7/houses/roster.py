import sys
from cs50 import SQL

if len(sys.argv) != 2:
    print("Usage ./python import.py <nameofthecsvfile>")
db = SQL("sqlite:///students.db")

house = sys.argv[1]
def func():
    b = db.execute("SELECT first,middle,last,birth FROM students WHERE house = '{}' ORDER BY last,first;".format(house))
    for i in range(len(b)):
        if b[i]["middle"] == None:
            print(b[i]["first"],b[i]["last"],end='')
            print(", born ", end='')
            print(b[i]["birth"])
        else:
            print(b[i]["first"],b[i]["middle"],b[i]["last"],end='')
            print(", born ", end='')
            print(b[i]["birth"])
func()






