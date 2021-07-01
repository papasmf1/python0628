# 메모리관리.py 

class MyClass:
    #초기화(인스턴스를 생성할 때 가장 먼저 실행)
    def __init__(self, value):
        self.value = value 
        print("Instance is created! value=", value)
    #인스턴스를 소멸할 때 가장 마지막에 실행 
    def __del__(self):
        print("Instance is deleted!")

d = MyClass(5)
#del d 
print("전체 코드 실행 종료")

