def move(n, fr, to, sapce):
	print str(n) + ' ' + 'from' + ' ' + str(fr) + 'to' + str(to)

def hanoi(n, fr, to, space):
	if n == 1:
		return move(n, fr, to, space)
	else:
		hanoi(n-1, fr, space, to)
		hanoi(1, fr, to, space)
		hanoi(n-1, space, to, fr)

hanoi(3, 'p', 'q', 'r')