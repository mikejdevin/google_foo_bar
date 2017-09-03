# foobar level 5
def answer(a,b,n):

    def paty2(t,m):
        if t<1:
            return []
        l = []
        if m<2:
            for i in range(1,t+1):
                l.append(1)
            return [l]
        for p in paty2(t,m-1):
            l.append(p)
        if t==m:
            l.append([m])
        if t>m:
            for p in paty2(t-m,m):
                q = [m]
                for i in p:
                    q.append(i)
                l.append(q)
        return l
    
    def gcd(a,b):
        while True:
            if a>b:
                a-=b
                continue
            if b>a:
                b-=a
                continue
            return a

    def gcdtab(a,b):
        t = []
        for i in range(1,a+1):
            l = []
            for j in range(1,b+1):
                l.append(gcd(i,j))
            t.append(l)    
        return t
    
    def fliplist(l):
        d = {}
        for i in l:
            d[i] = d.get(i,0)+1
        return d
    
    def fac(n):
        a = 1
        for i in range(1,n+1):
            a *= i
        return a

    def conjsize(p,t):
        num = fac(t) 
        for i in p:
            num /= i
        for k,v in fliplist(p).items():
            num /= fac(v)
        return num

    parta = paty2(a,a)
    partb = paty2(b,b)
    cytab = gcdtab(a,b)
    
    def gcdsum(p,q):
        s = 0
        for i in p:
            for j in q:
                s += cytab[i-1][j-1]
        return s

    tot = 0
    for p in parta:
        for q in partb:
            cs = conjsize(p,a)*conjsize(q,b)
            ci = gcdsum(p,q)
            tot += cs * ( n**ci )
    return (tot/fac(a))/fac(b)

#print answer(2,2,2)

