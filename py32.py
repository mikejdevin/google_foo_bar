def answer(n):    # your code here

    p = 0
    g = list(n)
    
    def incbn(a):
        i = 1
        x = 0
        while (x<1):
            x = (int(a[-i]) +1)%10
            a[-i]=str(x)
            i +=1
            if (i>len(a)):
                a.insert(0,'1')
                break
   
    def decbn(a):
        a[-1] = str(int(a[-1])-1)
    
    def divbn(a):
        i = 1
        while (i<len(a)+1):
            x = int(a[-i])
            a[-i] = str(int(x/2))
            if (x%2>0):
                y = int(a[1-i])+5
                a[1-i] = str(y)
            i +=1
        if (int(a[0])<1):
            a.pop(0)

    while (len(g)>1):
        print "".join(g) + "   " + str(p)
        p += 1
        z = int(g[-1])
        if (z%2<1):
            divbn(g)
            continue
        if (z%4<2):
            decbn(g)
            continue
        incbn(g)
    
    boo = int("".join(g))
    while ( boo > 1 ):
        print str(boo) +"   " + str(p)
        if boo==3:
            p +=2
            break
        p += 1
        if ( boo % 2 < 1 ):
            boo = boo/2
            continue
        if ( boo % 4 < 2 ):
            boo -= 1
            continue
        boo += 1
    return p
    
if (True):
    
    def incbn(a):
        i = 1
        x = 0
        while (x<1):
            x = (int(a[-i]) +1)%10
            a[-i]=str(x)
            i +=1
            if (i>len(a)):
                a.insert(0,'1')
                break
   
    def decbn(a):
        a[-1] = str(int(a[-1])-1)
    
    def divbn(a):
        i = 1
        while (i<len(a)+1):
            x = int(a[-i])
            a[-i] = str(int(x/2))
            if (x%2>0):
                y = int(a[1-i])+5
                a[1-i] = str(y)
            i +=1
        if (int(a[0])<1):
            a.pop(0)


q = "12345"

print "1   " + str(answer(q))



