import pymysql

def shopdb1_insert(name,price,company,contact):
    
    con = pymysql.connect(host = 'localhost', user = 'root', password = '1234', db = 'shopdb1', charset='utf8mb4')
    print("1. db 인증 -> 연결")
    print(con)
    
    cur=con.cursor()
    print("2. 연결정보 -> 통로 만들기 성공...")
    print(cur)
    
    sql = "insert into product values (" + name + ", " + price + ", " + company + ", " + contact +")"
    
    cur.execute(sql)
    print("3. sql문 만들어서 -> 전송 성공 ...")
    con.commit()
    
    cur.close()
    print("4. db 연결해제")