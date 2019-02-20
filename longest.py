import string
def longest(s):
	letter = string.letters[0:24]
	for i in range(len(s), -1, -1):
		#print i
		#print '----'
		for j in range(len(s) - i + 1):
			#print j
			#print s[j:i+j]
			if s[j:i+j] in letter:
				k = s[j:i+j]
				return k
				print 'Longest substring in alphabetical order is:', k

print longest('azcbobobegghakl')