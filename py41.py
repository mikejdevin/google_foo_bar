def answer(num_buns, num_required):
	# your code here
	combolist = {}
	def cccombo(a,b): # list of all binary reps of b choose a
		if (a<1):
			return [0]
		if (a==b): # pidgin holed
			return [ (1<<b) - 1 ]
		if (a==1): # 1 out of b
			w = []
			for i in range(0,b):
				w.append( 1 << i )
			return w
		num = a*100 +b #bad hash
		if combolist.has_key(num):
			return list(combolist[num])
		w = [ ( 1 << a ) - 1 ]
		for i in range(a,b):
			for n in cccombo(a-1,i):
				n += 1<<i
				w.append(n)
		combolist[num] = w
		return list(w)
	bunbun = []
	x = num_required - 1
	y = num_buns
	k = 0
	for j in range(0,y):
		bunbun.append([])
	ww = cccombo(x,y)
	for n in cccombo(x,y):
		z = n
		for j in range(0,y):
			if ((z%2)<1):
				bunbun[j].append(k)
			z = z / 2
		k += 1
	bunbun.sort()
	return bunbun
	

print answer(3,1)
print answer(2,2)
print answer(3,2)
print answer(5,3)



	