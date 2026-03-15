import random
import string

length = int(input(" Enter Password length ?"))

pword = string.ascii_letters + string.digits

pw = ''.join(random.choice(pword) for i in range (length))

print(pw)
#the longer length . the most safer
