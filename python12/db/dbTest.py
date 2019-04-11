import pymysql

def db_update(name,tel):

    '''1. db 인증 -> 연결'''
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    '''2. 연결정보 -> 통로'''
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    sql = "update member set tel = '" + tel + "' where name ='"+ name + "'"
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    '''4. db 연결해제'''
    cur.close()
    print("4. db 연결해제")

def db_insert(name,id,tel,addr):

    '''1. db 인증 -> 연결'''
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    '''2. 연결정보 -> 통로'''
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    # sql = "insert into member values ('400','400','400','400')"
    sql = "insert into member values ('" + name  + "', '"  + id  + "', '"+  tel   +"', '"+ addr +"')" 
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    '''4. db 연결해제'''
    cur.close()
    print("4. db 연결해제")
    

def db_delete(name):
    
    '''1. db 인증 -> 연결'''
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    '''2. 연결정보 -> 통로'''
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    sql = "delete from member where name = '" + name +"'"
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    '''4. db 연결해제'''
    cur.close()
    print("4. db 연결해제")
    
def db_select(name):
    
    
    '''1. db 인증 -> 연결'''
    con = pymysql.connect(host = 'localhost',
                          user = 'root', 
                          password = '1234', 
                          db = 'test') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    '''2. 연결정보 -> 통로'''
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    sql =  "select * from member where name = '"+ name + "'"
          
          
    cur.execute(sql)
    
    record = cur.fetchone()
    print(record)
    
    print(record[0],record[1],record[2],record[3])
    #===========================================================================
    # record = cur.fetchone()
    # print("검색된 name : ", record[0])
    # print("검색된 id : ", record[1])
    # print("검색된 tel : ", record[2])
    # print("검색된 addr : ", record[3])
    #===========================================================================
    
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    '''4. db 연결해제'''
    cur.close()
    print("4. db 연결해제")
    return record
    
    
if __name__ == '__main__':
    
    name = input("Name 입력 :")
    db_select(name)
    
    #===========================================================================
    # print("회원정보를 입력해주세요.")
    # name = input("Name 입력 :")
    # id = input("ID 입력 :")
    # tel = input("tel 입력 :")
    # addr = input("addr 입력 :")
    # db_insert(name,id,tel,addr)
    #===========================================================================
    
    #===========================================================================
    # print("삭제할 아이디 입력해주세요")
    # id = input("id 입력 :")
    # db_delete(id)
    #===========================================================================
    
    #===========================================================================
    # print("수정할 아이디 입력해주세요")
    # name = input("수정할 Name 입력 :")
    # tel = input("수정할 tel 입력 :")
    # addr = input("수정할 addr 입력 :")
    # id = input("수정할 ID 입력 :")
    # db_update(name, tel, addr, id)
    #===========================================================================
    
    
    
    