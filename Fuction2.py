# Fuction2.py 
#불변형식(int, float, tuple, str)
a = 1.2
print( id(a) )
a = 2.3 
print( id(a) )

print("---가변형식---")
#가변형식(99%)
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#전역변수와 지역변수가 충돌되는 경우
#LGB(Local, Global, Built-in)
#전역변수 초기화 
x = 5 
def func1(a):
    return x+a 

#호출 
print( func1(1) )

def func2(a):
    #지역변수를 초기화 
    x = 1 
    return x+a 

#호출 
print( func2(1) )

#가변형식의 경우는 입력 + 출력도 가능 
def change(x):
    #입력된 데이터의 복사본 생성(깊은 복사)
    x1 = x[:]
    x1[0] = "H"
    print("지역변수:", x1)

#함수 호출
wordlist = ["J","A","M"]
change(wordlist)
print(wordlist)

#불변형식의 전역변수를 함수 내부에서 읽기+쓰기
g = 1 
def testScope(a):
    #global g 
    g = 2 
    return a+g 

#함수호출
print( testScope(1) )
print("함수 호출후:", g)

#기본값 셋팅(default value)
def times(a=10, b=20):
    return a*b 

#호출
print( times() )
print( times(5) )
print( times(5,6) )

#키워드 인자(파라메터명을 기술)
def connectURI(server, port):
    str = "http://" + server + ":" + port 
    return str 

#호출
print( connectURI("credu.com", "80") )
print( connectURI(port="80", server="credu.com") )

