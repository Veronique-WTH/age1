password = 'a123456'
c = 3 # 剩餘機會
while True:
	pwd = input('please input password: ')
	if pwd == password:
		print('log in')
		break
	else:
		c = c - 1
		print('wrong! you have', c, 'times')
		if c == 0:
			break