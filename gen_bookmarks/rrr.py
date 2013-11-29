def x(c):
    print "ffff", c
    while True:
        line = yield
        if line in range(100):
            yield  line

            

matchers = [x("aaa"), x('bbb')]


for c in matchers: c.next()
#d = {matchers[0].send(c) : matchers[1].send(c) for c in range(100)}
d = dict((matchers[0].send(c), matchers[1].send(c)) for c in range(100))
## for c in range(1000):
##     a, b = matchers[0].send(c), matchers[1].send(c)
##     if a and b:
##         d[a] = b

