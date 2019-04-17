import pymysql

def db_insert(id,pw,name,personalNum,addr,email,num):

    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = "insert into member values ('" + id  + "', '"  + pw  + "', '"  + name  + "', '" +  personalNum   + "', '" + addr + "', '" + email + "', '" + num +"')" 
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
def db_update(id,pw,name,personalNum,addr,email,num):

    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = sql = "update member set pw = '" + pw + "', name = '" + personalNum + "', personalNum = '" + personalNum + "', addr = '"  + addr + "', email = '"  + email + "', num = '"  + num + "' where id = '" + id + "'"
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")

def db_delete(id):
    
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = "delete from member where id = '" + id +"'"
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
def db_select_id(name,personalNum):
    
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    sql =  "select * from member where name = '"+ name + "' and personalNum = '" + personalNum + "'"
          
    cur.execute(sql)

    record = cur.fetchone()
    
#     print(record)

#     print("검색된 id : ", record[0])
#     print("검색된 pw : ", record[1])
#     print("검색된 name : ", record[2])
#     print("검색된 personalNum : ", record[3])
#     print("검색된 addr : ", record[4])
#     print("검색된 email : ", record[5])
#     print("검색된 num : ", record[6])

    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
    return record

def db_select_pw(id):
    
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    sql =  "select * from member where id = '"+ id + "'"
          
    cur.execute(sql)
    
    record = cur.fetchone()
    
    print(record)

    print("검색된 pw : ", record[1])
#     print("검색된 pw : ", record[1])
#     print("검색된 name : ", record[2])
#     print("검색된 personalNum : ", record[3])
#     print("검색된 addr : ", record[4])
#     print("검색된 email : ", record[5])
#     print("검색된 num : ", record[6])

    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
    return record

