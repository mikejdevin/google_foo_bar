def answer(m , limit):

	loopdict = {}
	ironman = {}
	spool = {}
	
	def costfun(path):#cost of  path
		c = 0
		i = 0
		while i < len(path)-1:
			c += m[i][i+1]
			i += 1
		return c
	
	def lcostfun(path):#cost of a loop
		return costfun(path) + m[path[len(path)-1]][path[0]]

	def setify(path): # convert to set flags
		v = 0
		for i in path:
			v += 1 << path[i]
		return v

	def go(n): # generate all combinations
		if (n<1):
			return []
		i = 1
		j = 0
		bl = []
		while i <= n:
			if ( i & n ) < 1:
				j += 1
				i = i << 1
				continue
			if (n==i):
				return [ [ j ] ]
			b = go(n-i)
			for r in b:
				r.insert(0,j)
				bl.append(r)
			j += 1
			i = i << 1
		return bl	

	def costnoodle(paths):#cost of list of looppaths	
		yar = 99999
		for l in paths: 
			q = lcostfun(l)
			if q < yar:
				yar = q
		return yar

	def travelocity(paths): # cost of list of str paths
		yar = 99999
		for l in paths: 
			q = costfun(l)
			q += m[0][l[0]]
			q += m[l[len(l)-1]][maxnode-1]
			if yar > q:
				yar = q
		return yar

	def tpot(n): # number of ones in a number
		p = 0
		while n > 0:
			p += n%2
			n = n/2
		return p
	
	def loopaths():	# evaluate best simple loops of each nodeset
		for i in range(1,1 << maxnode ): # loop over possible sets of destinations
			if tpot(i) < 2: # ignore loops of one place
				continue
			lpl = go(i)# get all orders of the set
			loopdict[i] = costnoodle(lpl) #cost those orders

	def basepaths(): # get list of all nonrepeating paths from start to end
		for i in range(1,1 << maxnode - 1 ): # loop over possible sets of destinations
			if i % 2 > 0: # only odd numbers
				continue
			lpl = go(i) #get all orders of subset
			j = i + 1 + ( 1 << ( maxnode - 1 ) ) #append start and end
			ironman[j] = travelocity(lpl) #cost those orders
		ironman[1 + ( 1 << ( maxnode - 1 ) )] = m[0][maxnode-1]

	def ander(ir,lpd):#first join of loop to straight
		spool = {}
		for p in ir.keys():
			spool[p] = ir[p]
		for i in range(0,maxnode-1):
			for p in ir.keys():
				for q in lpd.keys():
					if (p & q) > 0:
						r = p | q
						x = ir[p]
						y = lpd[q]
						z = spool.get(r,limit+1)
						if x+y < z:
							spool[r] = x+y
			ir = spool
		return spool

	def weed(ir):#strip too long paths
		dum = {}
		for p in ir:
			if ir[p]>limit:
				continue
			dum[p] = ir[p]
		return dum

	def mostr():
		k = 0
		for i in spool.keys(): #find most places visited
			if spool[i] >limit:
				continue
			if tpot(i)>k:
				k=tpot(i)
		print "visits="+str(k)
		l = []
		if k<1:
			return []
		for i in spool.keys():
			if tpot(i)==k:
				l.append(i)
		l.sort()
		k = l[0]
		j = 0
		l = []
		while k>0:
			if k%2:
				l.append(j)
			k = k / 2
			j += 1
		l.pop(0)
		l.pop(len(l)-1)
		for i in range(0,len(l)):
			l[i] -= 1
		return l

	maxnode = len(m)
	loopaths() # calc all the simple loops
	basepaths() # calc simple nonloops
	ironman = weed(ironman)
	v = 0
	for p in ironman:
		if ironman[p]<v:
			v=ironman[p]
	print "base="
	print ironman
	v = limit - v
	lpd = {}
	for gg in loopdict.keys():
		if loopdict[gg] <0:# if neg loop, return all
			print "boink"
			return range(1,maxnode-1)
		if loopdict[gg] > v:
			continue
		lpd[gg] = loopdict[gg]
	print "loops="
	print lpd
	spool = ander(ironman,lpd) #band the groups together
	print "spool="
	print spool
	return mostr() #return longest trip0

def dynamouse(m,lim):
	n = len(m)
	roadhog = {}
	depth = 2*n - 2

	def gohous(x,t,d,p):
		if d<1:
			if x+1<n:
				return
			if roadhog.get(p,9000) > t:
				roadhog[p] = t
				return
		for i in range(0,n):
			if (x==i):
				continue
			gohous(i,t+m[x][i],d-1,p*n+i)

	gohous(0,0,depth,0)
	pew = {}
	for i in roadhog.keys():
		if roadhog[i] < lim+1:
			pew[i] = 1
	print pew
	

#ploo = [[0, 1, 1, 1, 1, 1 , 1], [1, 0, 1, 1, 1 ,1 ,1], [1, 1, 0, 1, 1,1,1], [1, 0, 1, 1, 1,1,1], [1, 1, 1, 1, 0,1,1],[1,1,1,1,1,0,1],[1,1,1,1,1,1,0]]
#ploo = [ [ 0,2,2,2,-1] , [9,0,2,2,-1] ,  [9,3,0,2,-1],[9,3,2,0,-1],[9,3,2,2,0]]
#ploo = [ [ 0  , 1 ] , [ 1 , 0 ] ]
#dynamouse(ploo,24)


#print answer( ploo ,1)

