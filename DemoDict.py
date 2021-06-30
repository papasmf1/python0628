# DemoDict.py 

device = {"아이폰":5, "아이패드":10,"윈도우":20}
print( device )
print( len(device) )
#입력 
device["맥프레"] = 15 
#수정 
device["아이폰"] = 6 
print( device )
#삭제
del device["아이폰"]
print( device )

#중단점, 중지점(Break Point)
for item in device.items():
    print(item)


for k,v in device.items():
    print(k,v)

#들여쓰기를 하는 경우는 
#본문이 있는 경우(함수를 정의, if else, for in) 
