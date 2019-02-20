def bobs(s):
	count = 0
	for i in range(len(s)-2):
		#print s[i:(i+3)]
		if s[i:(i+3)] == 'bob':
			count += 1
	return count

print(bobs('azcbobobegghakl'))