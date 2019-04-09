
def create(id, password, tel, addr):
    print("1. DB연결, 인증(id/pw)")
    sql = "insert into bbs values (" + id + ", " + password + ", " + tel + ", " + addr +")" 
    print("2.", sql, "insert문 실행 요청")
    print("3. DB 연결 해제..")
    
def read(id):
    print("1. DB연결, 인증(id/pw)")
    print("2. selert문 실행 요청")
    sql = "select from bbs where id = (" + id + ")"
    print("3.", sql, "검색결과를 받아와서 처리")
    print("4. DB 연결 해제..")
    
    result = []
    result.append("abc")
    result.append(1234)
    result.append(12345678)
    result.append("busan")
    return result

    id = "abc"
    password = 1234
    tel = 12345678
    addr = "busan"
      
    return id, password, tel, addr
     
    return (id, password, tel, addr)


def update(id,tel):
    print("1. DB연결, 인증(id/pw)")
    sql = "update form bbs set content(" + tel +") where id (" + id + ")"
    print("2.", sql, "update문 실행 요청")
    print("3. DB 연결 해제..")
    
def delete(id):
    print("1. DB연결, 인증(id/pw)")
    sql = "delete from bbs set (" + id + ")"
    print("2. insert문 실행 요청")
    print("3. DB 연결 해제..")
    
