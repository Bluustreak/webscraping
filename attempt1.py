from urllib.request import urlopen

def extractBetweenTags(content, tag):
    if "<" in tag or ">"  in tag:
        tag = tag.strip(['<', '>', '/'])
    startTag="<" + tag + ">"
    endTag="</" + tag + ">"
    startIndex = content.find(startTag) + len(startTag)
    endIndex = content.find(endTag)
    return content[startIndex:endIndex]

url = "http://olympus.realpython.org/profiles/poseidon"

page = urlopen(url)

html_bytes = page.read()

html = html_bytes.decode("utf-8")

print(extractBetweenTags(html, "title"))


print((lambda x:x*x)(2))