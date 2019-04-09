import memberDb


if __name__ == '__main__':

    print("---------게시판 등록 처리-----------")
    
    id = input("게시판 id입력 :")
    password = input("게시판 password입력 :")
    tel = input("게시판 tel입력 :")
    addr = input("게시판 addr입력 :")
        
    memberDb.create(id, password, tel, addr)
    
    print("---------게시판 검색 처리-----------")
    
    id = input("게시판 id입력 :")
    
    result = memberDb.read(id)
    
    print(result)
    
    
    a,b,c,d = memberDb.read(id)
      
    print(a, " ", b, " ", c, " ", d, " ")
    
    
    print(memberDb.read(id))


    print("---------게시판 삭제 처리-----------")
    id = input("게시판 id입력 :")
    memberDb.delete(id)
    
    
    print("---------게시판 수정 처리-----------")
    id = input("게시판 id입력 :")
    tel = input("게시판 tel입력 :")
    memberDb.update(id, tel)