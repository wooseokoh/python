import pymysql

def db_update(name,tel,addr,id):

    '''1. db 인증 -> 연결'''
    con = pymysql.connect(host = 'localhost',
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
    sql = "update member set name =" + name + ", tel =" + tel + ", addr =" + addr +", where id =" + id + ""
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
                          db = 'test', 
                          charset='utf8mb4') # 인증
    print("1. db 인증 -> 연결")
    print(con)
            
    '''2. 연결정보 -> 통로'''
    cur = con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    ''''3. sql문 만들어서 -> 전송'''
    # sql = "insert into member values ('400','400','400','400')"
    sql = "insert into member values (" + name + ", " + id + ", " + tel + ", " + addr +")" 
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    '''4. db 연결해제'''
    cur.close()
    print("4. db 연결해제")
    

def db_delete(id):
    
    '''1. db 인증 -> 연결'''
    con = pymysql.connect(host = 'localhost',
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
    sql = "delete from member where id =" + id
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    '''4. db 연결해제'''
    cur.close()
    print("4. db 연결해제")
    
if __name__ == '__main__':
    #===========================================================================
    # print("회원정보를 입력해주세요.")
    # name = input("Name 입력 :")
    # id = input("ID 입력 :")
    # tel = input("tel 입력 :")
    # addr = input("addr 입력 :")
    # db_insert(name,id,tel,addr)
    #===========================================================================
    
    print("삭제할 아이디 입력해주세요")
    id = input("id 입력 :")
    db_delete(id)
    
    #===========================================================================
    # print("수정할 아이디 입력해주세요")
    # name = input("수정할 Name 입력 :")
    # tel = input("수정할 tel 입력 :")
    # addr = input("수정할 addr 입력 :")
    # id = input("수정할 ID 입력 :")
    # db_update(name, tel, addr, id)
    #===========================================================================
    
    
    
    