# class1.py 
#클래스 형식을 정의
class Person:
    #초기화 메서드
    def __init__(self):
        #멤버 변수 초기화 
        self.name = "default name"
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스(복사본)만들기
p1 = Person() 
p1.print()
