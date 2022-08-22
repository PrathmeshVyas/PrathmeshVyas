import xml.dom.minidom

def main():
    doc = xml.dom.minidom.parse("samplexml.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    # get a list of XML tags from the document and print each one

    skills = doc.getElementsByTagName("skill")
    print("%d skills:" % skills.length)
    for s in skills:
        print(s.getAttribute("name"))

    #create new xml tag in document
    ns = doc.createElement('skill')
    ns.setAttribute("name", "Blockchain")
    doc.firstChild.appendChild(ns)

    skills = doc.getElementsByTagName("skill")

    print("%d skills:" % skills.length)
    for s in skills:
        print(s.getAttribute("name"))

main()