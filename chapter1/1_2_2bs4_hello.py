from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bs0bj = BeautifulSoup(html.read(), "html.parser")
# print(bs0bj.h1)
# print(bs0bj.div)
print(bs0bj.legend)


