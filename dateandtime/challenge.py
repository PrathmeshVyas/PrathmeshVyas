import calendar

def cd(ty, tm, wd):
    daycount=0

    weeklist = calendar.monthcalendar(ty, tm)
    for week in weeklist:
        if week[wd] != 0:
            daycount+=1
    return daycount


run = True
while(run):
    try:
        print("which day of the week you want to count ???")
        print("0: Monday:")
        print("1: tuesday:")
        print("2: wednesday:")
        print("3: thrusday:")
        print("4: friday:")
        print("5: saturday:")
        print("6: sunday:")

        theday = input("?? ")
        if theday==exit:
            run=False
            break

        day=int(theday)

        ys=input("enter year")
        y=int(ys)

        ms = input("enter month")
        m = int(ms)

        result=cd(y, m, day)
        print("there are  "+ str(result) + " of days in month and year")
        print("--------------------")
    except Exception as e:
        print(e)
        print("sorry invalid input")




