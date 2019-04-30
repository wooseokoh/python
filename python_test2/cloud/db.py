import pymysql

def insert(id,classes,content,cost,member):
    # db 인증 -> 연결
    con = pymysql.connect(host = 'localhost', 
                          user = 'root', 
                          password = '1234', 
                          db = 'class')
   
    print("1. db 인증 -> 연결")
    print(con)
    # 연결정보 -> 통로 만들기 성공
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)

    # sql문 만들고 전송하기
    sql = "insert into creg values ('" + id  + "', '"  + classes + "', '"  + content  + "', '" +  cost   + "', '" + member + "')" 
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()

    # db 연결해제
    cur.close()
    print("4. db 연결해제")
    
def printall():
    # db 인증 -> 연결
    con = pymysql.connect(host = 'localhost', 
                          user = 'root', 
                          password = '1234', 
                          db = 'class')
    # 연결정보 -> 통로 만들기 성공
    cur = con.cursor() 

    # sql문 만들고 전송하기
    sql =  "select * from creg"
    cur.execute(sql)
    record = cur.fetchall()

    # db 연결해제            
    cur.close()
    return record
    
def update(id,cost):
    # db 인증 -> 연결
    con = pymysql.connect(host = 'localhost', 
                          user = 'root', 
                          password = '1234', 
                          db = 'class')
    # 연결정보 -> 통로 만들기 성공
    cur = con.cursor() 

    # sql문 만들고 전송하기
    sql = "update creg set cost = '" + cost + "' where id = '" + id + "'"
    cur.execute(sql)

    con.commit()
    # db 연결해제
    cur.close()
    
def arrange():
    # db 인증 -> 연결
    con = pymysql.connect(host = 'localhost', 
                          user = 'root', 
                          password = '1234', 
                          db = 'class')
    # 연결정보 -> 통로 만들기 성공
    cur = con.cursor() 

    # sql문 만들고 전송하기
    sql =  "select * from creg"    
    cur.execute(sql)
    
    data = cur.fetchall()

    con.commit()
    # db 연결해제
    cur.close()
    
    return data


    

    
    