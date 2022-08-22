try:
    x=10/0
except:
    print("It didn't work")


try:

    answer=input("what should I divide by 10 ")
    num=int(answer)
    print(10/num)

except ZeroDivisionError as e:
    print("cant divide by zero")

except ValueError as e:
    print("Invalid Number")
    print(e)

finally:
    print("this code always runs")

