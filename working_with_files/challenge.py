import os

totalbytes = 0

dirlist = os.listdir()

for entry in dirlist:

    if os.path.isfile(entry):

        filesize = os.path.getsize(entry)
        totalbytes+=filesize


os.mkdir("results")

resultfile = open("results/results.txt", "w+")
if resultfile.mode=="w+":
    resultfile.write("totalbytecount: "+ str(totalbytes)+ "\n")
    resultfile.write("files list:\n")
    resultfile.write("------------\n")

for entry in dirlist:
    if os.path.isfile(entry):
        resultfile.write(entry + "\n")

resultfile.close()


