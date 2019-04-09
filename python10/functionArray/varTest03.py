def value(*parameter):
    print(len(parameter))
    print("전달받은 데이터 개수 :", len(parameter))
    
    for x in parameter:
        print(x, end = " ")
    print()
    
    
if __name__ == '__main__':
    value(1,2,3,4,5)
    value(123)
    value(1,2,34,5)