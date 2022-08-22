def func1():
    print("I am a programmer")


func1()
print(func1())
print(func1)


def func2(arg1, arg2):
    print(arg1, " ", arg2)


def func3(x):
    return x * x * x


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result


def multi_add(*args):
    result = 0
    for i in args:
        result = result + i
    return result


func2(10, 20)
print(func2(10, 20))
print(func3(7))

print(power(2))
print(power(2, 3))
print(power(x=3, num=2))

print(multi_add(2, 2, 4, 4))
