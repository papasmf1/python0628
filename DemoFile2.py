# DemoFile2.py 
#파일읽기와 쓰기 
f = open("c:/work/demo2.txt", "wt")
f.write("첫줄\n두번째줄\n세번째\n")
f.close()

print("파일을 닫은 여부:", f.closed)

#읽기 
f = open("c:/work/demo2.txt", "rt")
print( f.read() )
print( f.tell() )
#리셋
f.seek(0)
print(f.readline(), end="") 
print(f.readline(), end="") 
print("---리스트로 리턴---")
f.seek(0)
result = f.readlines() 
print(result)
f.close() 


