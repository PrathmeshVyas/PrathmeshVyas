import urllib.request

def main():
    weburl= urllib.request.urlopen("http://www.google.com")
    print("result code:", weburl.getcode())
    data = weburl.read()
    print(data)


main()