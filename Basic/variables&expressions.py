a=7
b=7.7
c="seven"
d=True
e=[1,2,3,4,5,6,7,8,9]
f={"one":1, "two":2}
g=(1,2,3,4,5)

intabc = "abs"

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(intabc)

print(e[1])
print(e[2])
print(e[1:5])
print(e[1:5:2])
print(e[::-1])

print(f['one'])


def some():
    global c
    c="def"
    print(c)

some()
print(c)

del c
print(c)