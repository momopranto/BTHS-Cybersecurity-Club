flag = 'flag{XXXXXXXXXXXXXXX}'
flag = flag.encode('hex').encode('rot13').encode('base64')
with open('secure1-encrypted.txt','w') as f:
    f.write(flag)
