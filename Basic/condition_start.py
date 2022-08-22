def main():
    x, y = 10, 100

    if x > y:
        print('greater')
    elif x==y:
        print('same')
    else:
        print("less")


    result = "x is less than y" if x < y else "x is less than or equal to y"
    print(result)

    value = 100
    # match value:
    #     case "one":
    #         result=1
    #     case "two":
    #         result = 2
    #     case "three" | "four":
    #         result = (3,4)
    #     case _:
    #         result = -1

    print(result)

if __name__ == '__main__':
    main()