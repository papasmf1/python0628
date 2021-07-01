# DemoFile.py 

import sys 

#숫자를 문자열로 변환
url = "http://www.credu.com/?page=" + str(1) 
print(url)

print("welcome to", "python", sep="~", end="!", file=sys.stderr)

#파일로 출력
f = open("c:/work/demo.txt", "wt")
print("file write", file=f)
f.close() 

#문자열을 오른쪽으로 정렬 
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).rjust(3) )
    
print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=", str(x*x).zfill(3) )
    
#16진수, 2진수 출력, 과학연산, 실수 출력 
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3))

