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


#파일에 영구적으로 저장할 경우
import pickle

colors = ["red","blue","green"]
print(colors)

f = open("c:/work/colors", "wb")
pickle.dump(colors, f)
f.close()

del colors 
#print("colors:", colors)

#다시 파일에서 복구 
f = open("c:/work/colors", "rb")
colors = pickle.load(f)
print(colors)
f.close() 

