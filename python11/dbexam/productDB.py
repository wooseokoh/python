import pymysql
from dbexam.product_insert import *
from dbexam.product_delete import *
from dbexam.product_select import *
from dbexam.product_update import *


num = 0

if __name__ == '__main__':
    
    while True:
        print("1.회원정보입력")
        print("2.회원정보삭제")
        print("3.회원정보선택")
        print("4.회원정보수정")
        print("5.종료")
        
        num = int(input("번호를 입력하세요. :"))
        
        if num == 1:    
            print("회원정보를 입력해주세요.")
            name = input("name 입력 :")
            price = input("price 입력 :")
            company = input("company 입력 :")
            contact = input("contact 입력 :")
            shopdb1_insert(name,price,company,contact)
            
        elif num == 2:
            print("삭제할 이름 입력해주세요")
            name = input("name 입력 :")
            shopdb1_delete(name)
            
        elif num == 3:
            print("선택할 이름 입력해주세요")
            name = input("name 입력 :")
            shopdb1_select(name)
            
        
        elif num == 4:
            print("수정할 가격 입력해주세요")
            price = input("수정할 가격 price 입력 :")
            name = input("name 입력 :")
            shopdb1_update(name,price)
        
        else:
            break
    
