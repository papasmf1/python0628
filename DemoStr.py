# DemoStr.py 

u = "<<<  spam and ham  >>>"
print(u)
#문자열 앞뒤에 문자들을 제거
result = u.strip("<> ") 
print(result)
#문자열을 치환
result = result.replace("spam", "spam and egg")
print(result)
#리스트로 리턴(공백문자를 기준) 
result2 = result.split() 
print(result2)
#다시 하나의 문자열로 합치기 
print( ":)".join(result2) )


#정규표현식(특정한 규칙을 가지고 있는 문자열 검색)
import re 

print( re.search("[0-9]*th", "35th") )
print( re.match("[0-9]*th", "35th") )
#검색 결과를 불린형식으로 리턴 
print( bool(re.search("[0-9]*th", "  35th")) )
print( bool(re.match("[0-9]*th", "  35th")) )

print("---apple---")
print( bool(re.search("apple", "this is apple")) )
print( bool(re.match("apple", "this is apple")) )

print("---우편번호---")
result = re.search("\d{5}", "우리동네는 52300")
print( result.group() )
result2 = re.search("\d{4}", "올해는 2021년")
print( result2.group() )

