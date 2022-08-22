def main():
    myfile = open("textfile.txt", "a+")

    for i in range(7):
        myfile.write("har har mahadeva\n")

    myfile.close()

    myfile=open("textfile.txt", "r")

    if myfile.mode=="r":
        # contents=myfile.read()
        # print(contents)
        fl = myfile.readlines()
        for x in fl:
            print(x)

main()
