# Function1.py 
#리턴을 하지 않는 함수
def setValue(newValue):
    x = newValue

#호출
result = setValue(5)
print(result)

#튜플을 리턴하는 함수
def swap(x,y):
    return y,x 

#호출
result = swap(5,6)
print(result)
print(result[0])
print(result[1])

#교집합을 리턴하는 함수
def intersect(prelist, postlist):
    #카멜 표기법(첫단어는 소문자로 나머지는 첫글자만 대문자)
    #교집합 문자를 저장할 지역 변수
    retList = []
    #H(0) | A(1) | M(2)
    for x in prelist:
        #어떤 글자가 postlist에 포함되어 있고 그리고 retList 아직 없다. 
        if x in postlist and x not in retList:
            retList.append(x)
    return retList 

#함수 호출
print( intersect("HAM","SPAM") )
