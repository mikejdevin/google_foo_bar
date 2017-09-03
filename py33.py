# checksum challenge

import math

def tobit(n):
	a = []
	b = int(n)
	i = 0
	while i<31:
		a.append(b%2)
		b = b / 2
		i +=1
	return a

def tonum(l):
	l.reverse()
	n = 0
	while len(l)>0:
		n *= 2
		n += l[0]
		l.pop(0)
	return n

def duck(r,f):
	r = r % f
	if r < (f>>1):
		return 0
	return (r - (f>>1)) % 2

def goos(n):
	w = ( n /2) % 2
	for i in range(1,31):
		w += duck(n,2<<i) << i
	return w

def groot(a,b):
	x = goos(a)
	y = goos(a+b)
	x = x ^ y
	return x

def hoot(a,b):
	i = 0
	x = 0
	s = a
	while i<b:
		y = groot(s,s+b-i)
		i +=1
		s +=b
		x = x^y
	return x

print hoot(10,45000)

def broot(a,b):
	x = a
	for i in range(1,b):
		x = x ^ ( x + i )
	return x



#def broot(a,b):
#	x = tobit(a)
#	for i in range(a+1,a+b):
#		y = tobit(i)
#		for i in range(0,31):
#			x[i] = ( x[i] + y[i] ) % 2
#	return x		
#
#e = []
#for i in range(0,100):
#	for j in range(0,100):
#		if (tonum(groot(i,j)) - tonum(broot(i,j)))>0:
#			e.append(i*1000+j)
#print e



