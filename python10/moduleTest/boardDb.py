
def create(id, title, content, writer):
    print("1. DB연결, 인증(id/pw)")
    sql = "insert into bbs values (" + id + ", " + title + ", " + content + ", " + writer +")" 
    print("2.", sql, "insert문 실행 요청")
    print("3. DB 연결 해제..")
    
def read(id):
    print("1. DB연결, 인증(id/pw)")
    print("2. selert문 실행 요청")
    sql = "select from bbs where id = (" + id + ")"
    print("3.", sql, "검색결과를 받아와서 처리")
    print("4. DB 연결 해제..")
    
    result = []
    result.append(100)
    result.append(100)
    result.append(100)
    result.append(100)
    return result
    
    #===========================================================================
    # id = 100
    # title = 100
    # content = 100
    # writer = 100
    # 
    # return id,title,content,writer
    #===========================================================================
#     return "select한 결과 반환.."
    
def update(id,content):
    print("1. DB연결, 인증(id/pw)")
    sql = "update form bbs set content(" + content +") where id (" + id + ")"
    print("2.", sql, "update문 실행 요청")
    print("3. DB 연결 해제..")
    
def delete(id):
    print("1. DB연결, 인증(id/pw)")
    sql = "delete from bbs set (" + id + ")"
    print("2. insert문 실행 요청")
    print("3. DB 연결 해제..")
    
