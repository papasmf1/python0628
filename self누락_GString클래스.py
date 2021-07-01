#전역변수와 멤버변수가 충돌나는 경우 
str = "Not Class Member"

class GString:
    def __init__(self):
        #인스턴스 멤버 변수를 초기화 루틴 
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #약간의 버그 
        print(self.str)

g = GString()
g.set("First Message")
g.print()
