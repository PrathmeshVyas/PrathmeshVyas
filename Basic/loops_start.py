def main():
    x = 0

    while x<5:
        print(x)
        x+=1

    d=["mon","tue","wed","thrus","fri","sat","sun"]
    for d in d:
        print(d)

    for x in range(5, 10):
        print(x)

    for x in range(5, 10):
        # if x==7:
        #     break
        if x%2==0:
            continue
        print(x)


    d = ["mon", "tue", "wed", "thrus", "fri", "sat", "sun"]
    for i,d in enumerate(d):
        print(i, d)
if __name__ == '__main__':
    main()