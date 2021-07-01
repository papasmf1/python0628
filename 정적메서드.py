# 정적메서드.py
class MyCalc(object):
    #정적 메서드는 클래스에서 호출
    #데코레이터를 사용해서 명시 
    @staticmethod
    def my_add(x,y):
        return x+y
    #인스턴스 메서드는 인스턴스에서 호출
    def methodA(self):
        print("methodA()호출")

#클래스에서 직접 호출한다.
a = MyCalc.my_add(5,7)
print(a)

calc = MyCalc()
calc.methodA() 

