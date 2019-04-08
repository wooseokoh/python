'''
Created on 2019. 4. 8.

@author: user
'''
import random
import string



def password():
    _LENGTH = 10
    r_password = string.ascii_letters+string.digits
    result = ""
    for x in range(_LENGTH):
        result += random.choice(r_password)
    print(result)


if __name__ == '__main__':
    for x in range(0,3):
        password()


