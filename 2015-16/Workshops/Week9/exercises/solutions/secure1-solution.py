with open('secure1-encrypted.txt') as f:
    flag = f.read()
    print flag.decode('base64').decode('rot13').decode('hex')
