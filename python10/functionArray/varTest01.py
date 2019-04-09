count = 0

def javaCount():
    global count
    count = count + 1
    print(count)

def pythonCount():
    global count
    count = count + 1
    print(count)
    
if __name__ == '__main__':
    
    javaCount()
    pythonCount()
    javaCount()
    pythonCount()
    javaCount()
    pythonCount()