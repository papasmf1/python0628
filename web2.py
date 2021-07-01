# web2.py 
#웹서버와 통신(요청)
import urllib.request
#크롤링
from bs4 import BeautifulSoup

#웹서버에서 페이지를 실행한 결과를 문자열로 받기 
data = urllib.request.urlopen("http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri")
#검색이 용이한 객체 생성
soup = BeautifulSoup(data, "html.parser")

cartoons = soup.find_all("td", class_="title")
# ctrl + / 
# <td class="title">
# 		<a href="/webtoon/detail.nhn">마음의 소리 50화 &lt;격렬한 나의 하루&gt;</a>
# </td>
title = cartoons[0].find("a").text 
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#반복 구문(10개)
#파일에 저장 
f = open("c:/work/webtoon.txt", "wt", encoding="utf-8")
for item in cartoons:
    title = item.find("a").text 
    print(title)
    f.write(title + "\n")

f.close() 

