def vowels(s):
	k = 0
	for i in ['a', 'e', 'i', 'o', 'u']:
		#print s.count(i)
		k = k + s.count(i)
	print 'number of vowels:', k
	return k
