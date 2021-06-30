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
