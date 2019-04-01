money = int(input("돈을 입력하세요 :"))

c1000 = money // 1000
print("1000원짜리 ",c1000,"개")
    
etc = money % 1000
print("나머지 ",etc,"원")
    
c500 = money // 500
print("500원짜리 ",c500,"개")
    
etc = money % 500
print("나머지 ",etc,"원")
    
c100 = money // 100
print("100원짜리 ",c100,"개")
    
etc = money % 100
print("나머지 ",etc,"원")

c10 = money // 10
print("10원짜리 ",c10,"개")
    
etc = money % 10
print("1원짜리 ",etc,"개")