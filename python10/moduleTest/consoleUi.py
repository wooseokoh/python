import boardDb


if __name__ == '__main__':
    
    print("---------게시판 검색 처리-----------")
    
    id = input("검색할 id 입력 :")
    
    result = boardDb.read(id)
    
    print(result)
    
    #===========================================================================
    # a,b,c,d = boardDb.read(id)
    #  
    # print(a, " ", b, " ", c, " ", d, " ")
    #===========================================================================
    
    #===========================================================================
    # print(boardDb.read(id))
    # 
    # result = boardDb.read(id)
    # print(result)
    #===========================================================================
    
    
    print("---------게시판 등록 처리-----------")
    
    id = input("게시판 id입력 :")
    title = input("게시판 title입력 :")
    content = input("게시판 content입력 :")
    writer = input("게시판 writer입력 :")
       
    boardDb.create(id, title, content, writer)
        
    
    print("---------게시판 삭제처리-----------")
    id = input("게시판 id입력 :")
    boardDb.delete(id)
    
    print("---------게시판 수정 처리-----------")
    id = input("게시판 id입력 :")
    content = input("게시판 content입력 :")
    boardDb.update(id, content)
    