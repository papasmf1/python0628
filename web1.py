# web1.py 

#from 패키지명 import 모듈명
from bs4 import BeautifulSoup

#웹페이지를 로딩(메서드를 연속으로 호출할 수 있음)
#유니코드를 읽기와 쓰기를 할 경우 인코딩방식을 지정 
#page는 문자열 변수(문서)
page = open("c:/work/test01.html", "rt", encoding="utf-8").read() 
#검색이 용이한 객체(인터넷상에 있는 html문서를 검색)
soup = BeautifulSoup(page, "html.parser")
#멋지게 보여달라~~
#print( soup.prettify() )

#<p>태그를 모두 가져오기 ==> 리스트 형식으로 리턴
#print( soup.find_all("p") )

#<a>태그 
#print( soup.find_all("a") )

#첫번째 <p>만 가져오기 
#print( soup.find("p") )

#조건이 있는 경우: <p class="outer-text">
#파이썬 언어에서 class는 타입을 정의하는 구문
#print( soup.find_all("p", class_="outer-text") )

#태그 내부에 컨텐츠만 검색(text속성을 사용) 
for tag in soup.find_all("p"):
    print( tag.text.replace("\n", "").strip() )

