# DemoLoop.py 

#반복구문
value = 5 
while value > 0:
    print(value)
    value -= 1 

#변수명이 반드시 문자로 시작해야 된다! first1 second2 
lst = [100, 3.14, "apple"]
for item in lst:
    print(item, type(item))

#구구단을 출력
#외곽에 있는 반복구문(outer)
for x in [2,3,4,5,6]:
    print("--{0}단--".format(x))
    #내부에 있는 반복(inner)
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x, y, x*y))

#반복구문을 탈출 
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break 
    print("Item:{0}".format(i))

print("----continue----")
#continue는 지속적으로 수행(약간의 스킵)
for i in lst:
    if i % 2 == 0:
        continue 
    print("Item:{0}".format(i))

#수열함수 
print( list(range(10)) )
print( list(range(1,11)) )
print( list(range(10,0,-1)) )
#수동으로 반복을 5번 
for i in range(5):
    print(i)

#리스트 컴프리헨션(함축, 압축)
lst = [1,2,3,4,5,6,7,8,9,10]
#전체 리스트에서 필터리을 하고 가공 
print( [i**2 for i in lst if i > 5] )

d = {100:"apple", 200:"kiwi", 300:"orange"}
print( [v.upper() for v in d.values()] )

#필터링하는 함수
lst = [10, 25, 30]
iterL = filter(None, lst)
for i in iterL:
    print("Item:{0}".format(i))

print("---필터링---")
#함수를 정의(4장)
def getBiggerThan20(i):
    return i > 20

iterL = filter(getBiggerThan20, lst)
for i in iterL:
    print("Item:{0}".format(i))

