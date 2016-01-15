with open('secure2-encrypted.txt') as f:
    flag = f.read()
    while True:
	if 'flag' in flag:
	    print flag
	    break
	else:
	    flag = flag.decode('base64')
