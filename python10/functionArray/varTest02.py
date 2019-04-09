
def call(x,y,z):
    sum = x+y+z
    print(sum/3)
    
def call2(x,y,z=0):
    sum = x+y+z
    print(sum/3)


if __name__ == '__main__':

    call(100,88,50)
    call2(100,88)
    