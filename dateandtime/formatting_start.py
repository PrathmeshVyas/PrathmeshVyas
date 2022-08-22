from datetime import datetime

def main():
    now=datetime.now()

    # date formatting

    print(now.strftime("the current year is: %Y"))
    print(now.strftime("%a, %d, %B, %y"))
    print(now.strftime("local date&time: %c"))
    print(now.strftime("local date: %x"))
    print(now.strftime("local time: %X"))

    print(now.strftime("current-time: %I:%M:%S %p"))
    print(now.strftime("24 hrs-time: %H:%M:%S %p"))


main()