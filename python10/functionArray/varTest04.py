def value(**parameter):
    print("전달받은 데이터 개수 :", len(parameter))
    for x in parameter.keys():
        print(x ," : ", parameter[x], end = " ")
        print()
    
if __name__ == '__main__':
    value(감자 = 10, 고구마 = 20, 양파 = 30)