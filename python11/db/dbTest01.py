import pymysql

'''1. db 인증 -> 연결'''
con =pymysql.connect(host = 'localhost',
                     user = 'root', 
                     password = '1234', 
                     db = 'test', 
                     charset='utf8mb4') # 인증

print("1. db 인증 -> 연결")
print(con)
        
'''2. 연결정보 -> 통로'''
cur = con.cursor()
print("2. 연결정보 -> 통로 만들기 성공...")
print(cur)

''''3. sql문 만들어서 -> 전송'''
sql1 = "insert into member values ('111','111','111','111')"
sql2 = "insert into member values ('222','222','222','222')"
sql3 = "insert into member values ('333','333','333','333')"

result = cur.execute(sql1)
print("sql문 실행결과 :", result) # 값이 잘들어갔다는 결과값 1
result = cur.execute(sql2)
print("sql문 실행결과 :", result)
result = cur.execute(sql3)
print("sql문 실행결과 :", result)

print("3. sql문 만들어서 -> 전송 성공 ...")
con.commit()

'''4. db 연결해제'''
cur.close()
print("4. db 연결해제")



