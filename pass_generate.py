import string
import random



def gen_password(length):
    pickable = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation; 
    password = ''.join(random.choice(pickable) for i in range(length))
    print('Password Suggestion :', password)

if __name___=='__main':
    leng = int(input('Enter the Length of Password you want to generate: '))
    gen_password(leng)
