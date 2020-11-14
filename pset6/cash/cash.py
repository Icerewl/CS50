from cs50 import get_float
import sys

while True:
    cash = get_float("Change owed: ")
    #print(cash)
    if cash > 0:
        rounded = float(cash) * 100
        #print(rounded)

        a = int(rounded) / 25
        b = int(rounded) % 25

        c = int(b) / 10
        d = int(b) % 10

        e = int(d) / 5
        f = int(d) % 5

        g = int(f) / 1
        h = int(f) % 1

        pennies = int(a) + int(c) + int(e) + int(g)

        print(int(pennies))
        sys.exit(0)





    else:
        cash = get_float("Change owed: ")


