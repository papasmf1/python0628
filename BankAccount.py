# BankAccount.py

#은행의 계정을 표현한 클래스 
class BankAccount:
    #초기화 메서드
    def __init__(self, id, name, balance):
        #멤버변수를 숨기는 경우는 __변수명 이름 변경을 요구
        self.__id = id
        self.__name = name 
        self.__balance = balance
    #입금 메서드  
    def deposit(self, amount):
        self.__balance += amount 
    #출금 메서드 
    def withdraw(self, amount):
        self.__balance -= amount
    #객체의 문자열을 리턴하는 메서드 
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)
print(account1)
#백도어(테스트하는 용도)
print(account1._BankAccount__balance)




