import time 

def routine1():
    c = 0
    g = []
    while c != 5000000:
        g.append(c)
        c += 1
        yield R2
    print  g[-1]
    yield R2
    
def routine2():
    c= 10000000
    g = []
    while c != 5000000:
        g.append(c)
        c -= 1
        yield R1
    print  g[-1]

## R1, R2 = routine1(), routine2()
## current = R1
## start = time.time()
## while True:
##     try: current = current.next()
##     except StopIteration:
##         print "stop"
##         break
def x():
    c = 0
    g=[]
    while c !=5000000:
        g.append(c)
        c +=1
    return g[-1]
def y():
    c= 10000000
    g= []
    while c!= 5000000:
        g.append(c)
        c -= 1
    return g[-1]
start = time.time()
print x()
print y()
print "TIME => ",time.time() - start
