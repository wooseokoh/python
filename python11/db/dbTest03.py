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

sql = "select * from member where id = '111'"
result = cur.execute(sql)
print("sql문 실행결과 :",result)
print("3. sql문 만들어서 -> 전송 성공 ...")

# print(cur.fetchone()) 레코드 하나를 불러올떄
record = cur.fetchone()
print("검색된 name : ", record[0])
print("검색된 id : ", record[1])
print("검색된 tel : ", record[2])
print("검색된 addr : ", record[3])

con.commit()

'''4. db 연결해제'''
cur.close()
print("4. db 연결해제")



