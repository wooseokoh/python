import pymysql

def db_insert(id,title,content,director,img):

    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = "insert into movie values ('" + id  + "', '"  + title  + "', '"+  content   +"', '"+ director +"', '"+ img +"')" 
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
def db_update(id,title,content,director,img):

    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = sql = "update movie set title= '" + title + "', content = '" + content + "', director = '"  + director + "', img = '"  + img + "' where id = '" + id + "'"
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
    
    sql = "delete from movie where id = '" + id +"'"
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
def db_select(id):
    
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
    sql =  "select * from movie where id = '"+ id + "'"
          
    cur.execute(sql)
    
    record = cur.fetchone()
    
    print(record)

    print("검색된 id : ", record[0])
    print("검색된 title : ", record[1])
    print("검색된 content : ", record[2])
    print("검색된 director : ", record[3])
    print("검색된 img : ", record[4])

    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")
    
    return record

def db_select_all():
    
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
    sql =  "select * from movie"
    print("생성된 sql :", sql)
    n = cur.execute(sql)
    # 연결통로 (파이썬에서만 사용)
    result = []

    print("3. sql문 만들어서 -> 전송 성공 ...")
#     con.commit()
    while True:
        record = cur.fetchone() # 하나씩 읽어오기
        if record == None:
            break
        else:
            print(record)
            result.append(record)
#     print(result)
        
    cur.close()
    print("4. db 연결해제")
    
    return result

if __name__ == '__main__':
#     db_select_all()
    result = db_select_all()
    print("내가 받아온 리스트 :", result)


