def vowels(s):
	l = []
	for i in ['a', 'e', 'i', 'o', 'u']:
		#print s.count(i)
		k = s.count(i)
		#print k
		l.append(k)
	return l


#print vowels('aeiou')