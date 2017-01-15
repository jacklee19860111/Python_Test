import urllib
url="http://www.iplaypython.com"
html = urllib.urlopen(url)
print html.info()
url = "http://www.163.com"
html = urllib.urlopen(url)
print html.info()
print html.getcode()

