# Function2.py 
#가변인자를 처리(합집합을 리턴)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출 
print( union("HAM", "EGG") )
print( union("HAM", "EGG", "SPAM") )

#정의되지 않은 인자 처리(딕셔너리로 받기)
def userURIBuilder(server, port, **user):
    str = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        str += key + "=" + user[key] + "&"
    return str 

#호출
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234"))
print( userURIBuilder("credu.com", "80", id="kim", passwd="1234", 
    name="mike", age="30"))

