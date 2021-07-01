# coding:utf-8
from bs4 import BeautifulSoup
import urllib.request
#정규 표현식(내가 원하는 문자열만 검색)
import re 

#웹봇:자동으로 데이터를 수집(금지)
#User-Agent를 조작하는 경우(아이폰에서 사용하는 사파리 브라우져의 헤더) 
hdr = {'User-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.23 (KHTML, like Gecko) Version/10.0 Mobile/14E5239e Safari/602.1'}




#한페이지는 30개 * 10개 페이지 ==> 300 
for n in range(0,10):
        #클리앙의 중고장터 주소 
        data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
        print(data) 
        #웹브라우져 헤더 추가 
        req = urllib.request.Request(data, \
                                    headers = hdr)
        #실행결과를 문자열 변수로 받기
        data = urllib.request.urlopen(req).read()
        #혹시 한글이 깨지면 디코딩 방식(해석)
        page = data.decode('utf-8', 'ignore')
        soup = BeautifulSoup(page, 'html.parser')

        #블럭 주석처리: ctrl + / 
        # <span class="subject_fixed" data-role="list-title-text">
        #       아이폰 12 mini red 64기가 판매합니다.
        # </span>

        #attrs ==> 속성들 
        list = soup.find_all('span', attrs={'data-role':'list-title-text'})

        for item in list:
                try:
                        title = item.text 
                        if (re.search('맥북', title)):
                                print(title.strip())
                                
                except:
                        pass
        
