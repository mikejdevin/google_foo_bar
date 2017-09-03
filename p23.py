import math
import random

if (True):
    
    xs = [ ]
    i = 0
    gg = 1
    while i < 50:
        i += 1
        z = random.randint(2,999)
        gg = gg * z
        xs.append(z)
    
    ng = []
    ps = []
    
    for i in range(len(xs)) :
        if (xs[i]>0):
            ps.append(xs[i])
        if (xs[i]<0):
            ng.append(xs[i])
    ng.sort(reverse = True)
    print str(ng)
    if ( len(ng) % 2 ):
        print "pop"
        ng.pop(0)
    for i in range(len(ng)) :
        ps.append(-ng[i])
    ps.sort()    
    print str(ps)
    bn = [ 1 ]
    if (len(ps)<1):
        print "0"
    for n in range(len(ps)) :
        nn = []
        carry = 0
        for m in range(len(bn)) :
            q = bn[m] * ps[n] + carry
            nn.append( q % 10000 )
            carry = int(q / 10000) 
        if (carry>0):
            nn.append(carry)
        bn = nn
    s = ""      
    sa = ""
    for n in range(len(bn)) :
        sa = str(bn[n]).rjust(4,'0')
        s = sa + s
        print sa
    
    while s.startswith("0"):
        s = s[1:]
    
    print int(s)- gg