# Function2.py 
#가변인자를 처리(합집합을 리턴)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출 
print( union("HAM", "EGG") )
print( union("HAM", "EGG", "SPAM") )

#정의되지 않은 인자 처리(딕셔너리로 받기)
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

#호출
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234"))
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234", 
    name="mike", age="30"))


#람다 함수(이름이 없는 간단한 함수 정의 문법)
g = lambda x,y:x*y 
print( g(3,4) )
print( g(5,6) )
print( (lambda x:x*x)(3) )
print( globals() )

#pass라는 키워드
class Temp:
    pass 

#함수를 정의(도움말) __doc__
def add(a,b):
    """이 함수는 2개의 숫자를
        입력받아서 덧셈을 합니다."""
    return a+b 

#호출
print( help(add) )

#순회가능한 형식은 빠르게 열거하는 for in 루프를 사용 
for char in "abc":
    print(char)

#제너레이터 형식:yield구문을 사용하는 경우 
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

#호출
for char in reverse("gold"):
    print(char)

#단순하게 만든 예제 
#yield(값을 생성하고 추출하고 마지막에 반환)
print("---abc()---")
def abc():
    s = "abc"
    for char in s:
        yield char 

#호출
for char in abc():
    print(char)


