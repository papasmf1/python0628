# class2.py 

#클래스 형식을 정의
class Person:
    #주로 데이터 공유가 목적(static)
    num_person = 0 
    #초기화 메서드
    def __init__(self):
        #멤버 변수 초기화 
        self.name = "default name"
        Person.num_person += 1 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본)만들기
p1 = Person() 
p2 = Person()
p3 = Person() 
print("인스턴스 갯수:{0}".format(Person.num_person) )
p1.name = "전우치"
p2.name = "홍길동"
p1.print()
p2.print()

#런타임(실행시간)시에 변수를 추가(동적인 언어의 특징)
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)


