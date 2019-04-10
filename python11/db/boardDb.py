
def create(name,id,tel,addr):
    print("1. DB연결, 인증(id/pw)")
    sql = "insert into member values (" + name + ", " + id + ", " + tel + ", " + addr +")" 
    print("2.", sql, "insert문 실행 요청")
    print("3. DB 연결 해제..")
    
def read(id):
    print("1. DB연결, 인증(id/pw)")
    print("2. selert문 실행 요청")
    sql = "select from member where id = (" + id + ")"
    print("3.", sql, "검색결과를 받아와서 처리")
    print("4. DB 연결 해제..")
    

def update(id,addr):
    print("1. DB연결, 인증(id/pw)")
    sql = "update form member set addr(" + addr +") where id (" + id + ")"
    print("2.", sql, "update문 실행 요청")
    print("3. DB 연결 해제..")
    
def delete(id):
    print("1. DB연결, 인증(id/pw)")
    sql = "delete from member set (" + id + ")"
    print("2. insert문 실행 요청")
    print("3. DB 연결 해제..")
    
