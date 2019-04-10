import pymysql

def shopdb1_select(name):
    
    con = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'shopdb1', charset='utf8mb4')
    print("1. db 인증 -> 연결")
    print(con)
    
    cur=con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = "select * from product where name ="+name
    
    cur.execute(sql)

    
    record = cur.fetchone()
    print("검색된 name : ", record[0])
    print("검색된 id : ", record[1])
    print("검색된 tel : ", record[2])
    print("검색된 addr : ", record[3])
    
    
    
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")