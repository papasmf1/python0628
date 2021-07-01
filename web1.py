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
print( soup.prettify() )
