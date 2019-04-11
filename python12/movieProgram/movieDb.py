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
    
    sql = sql = "update movie set title= " + title + ", content = " + content + ", director = "  + director + " where id = " + id
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

if __name__ == '__main__':
    
    
    print("회원정보를 입력해주세요.")
    id = input("ID 입력 :")
    title = input("title 입력 :")
    content = input("content 입력 :")
    director = input("director 입력 :")
    img = input("img 입력 :")
    db_insert(id,title,content,director,img)

