# 메모리구조.py
#부모 클래스 
class SuperClass:
    #초기화(생성자)
    def __init__(self):
        self.x = 10 
    def printX(self):
        print(self.x)

#자식 클래스 
class SubClass(SuperClass):
    #초기화 메서드를 덮어쓰기 
    def __init__(self):
        #대부분은 부모의 생성자 메서드를 명시적으로 호출해야 된다.
        SuperClass.__init__(self)
        self.y = 20
    def printY(self):
        print(self.y)

#인스턴스 생성 
s = SubClass()
s.a = 30 
# 블럭으로 주석: ctrl + / 
# print("SuperClass:", SuperClass.__dict__)
# print("SubClass:", SubClass.__dict__)
# print("s:", s.__dict__)
s.printX()
s.printY()
