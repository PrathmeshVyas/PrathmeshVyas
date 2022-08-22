string = input("enter a string to check ")

string=string.lower()


if string==string[::-1]:
    print(True)
    print(string)
else:
    print(False)

