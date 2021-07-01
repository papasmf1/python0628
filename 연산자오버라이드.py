#연산자 오버라이드 
class NumBox:
	def __init__(self, num):
		self.Num = num
	# +연산자의 의미를 변경해서 사용
	# 일반 메서드로 구현  
	def add(self, num):
		self.Num += num
	# -연산자를 변경 
	def remove(self, num):
		self.Num -= num

#인스턴스 생성
n = NumBox(40)
n.add(100)
print(n.Num)
n.remove(40)
print(n.Num)
