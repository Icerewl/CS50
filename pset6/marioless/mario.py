while True:
    try:

        height = input("Height: ")
        while 9 > int(height) > 1:
            i = 0
            while i <= int(height):
                a = int(height) - i

                print(a * ' ' + "#" * i)

                i = i + 1
            exit()
    except ValueError:
        print("invalid number please try again")
    except TypeError:
        print("Please try a positive number")
