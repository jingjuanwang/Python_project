def for_loop(s):
	count = 0
	for i in range(len(s)-2):
		print s[i:(i+3)]
		if s[i:(i+3)] == 'bob':
			count += 1
	print count
for_loop('azcbobobegghakl')