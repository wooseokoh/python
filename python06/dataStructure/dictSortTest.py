import operator
 
data1 = {1: "송아무개",3: "김아무개",2: "박아무개"}
 
data2 = sorted(data1.items(), key=operator.itemgetter(0), reverse=False)
data3 = sorted(data1.items(), key=operator.itemgetter(1), reverse=False)
 
print(data2)
print(data3)




                            
            












