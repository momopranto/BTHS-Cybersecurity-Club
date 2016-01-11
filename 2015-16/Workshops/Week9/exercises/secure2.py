import random

flag = 'flag{XXXXXXXXXXXXXXXX}'
for i in range(random.randint(0,100)):
    flag = flag.encode('base64')

with open('secure2-encrypted.txt','w') as f:
    f.write(flag)
