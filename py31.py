# google challenge 3-1

d = {}


def subf(n,m):
    if (n<1):
        return 0 #no briks
    if (m<1): # no room
        return 0
    if (m*(m+1)<2*n):
        return 0 # too many briks
    if (n<3): # base cases
        return 1
    k = n*1000+m
    if d.has_key(k):
        return d[k]
    if (n>m):
        s = 0
        for i in range(1,m+1):
            s += subf(n-i,i-1)
    if (n<m+1):
        s = 1
        for i in range(1,n):
            s += subf(n-i,i-1)
            
    d[k] = s
    return s

def f(a):
    s = 0
    for i in range(1,a):
        s += subf(a-i,i-1)
    return s

print f(200)