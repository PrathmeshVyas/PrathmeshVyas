from html.parser import HTMLParser

class myhtmlparser(HTMLParser):
    def handle_comment(self, data):
        pass
    def handle_data(self, data):
        pass
    def handle_starttag(self, tag, attrs):
        pass

def main():
    #  initiate the parser and feed it some html

    parser = myhtmlparser()

    f = open("samplehtml.html")
    if f.mode == 'r':
         c = f.read() #read entire file
         parser.feed(c)

main()