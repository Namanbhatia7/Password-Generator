import string
import random



def gen_password(length):
    
    case1 = string.ascii_lowercase;
    case2 = string.ascii_uppercase;
    case3 = string.digits;
    case4 = string.punctuation;
    pickable = case1 + case2 + case3 + case4
    password = ''.join(random.choice(pickable) for i in range(length))
    print('Password Suggestion :', password)



leng = int(input('Enter the Length of Password you want to generate: '))

gen_password(leng)


