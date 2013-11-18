def routine1(data):
    print "A", data,;
    data = yield(R2,'a')
    print "B", data,;
    data = yield(R2, 'b')

def routine2(data):
    data = yield
    print "C", data,;
    data = yield(R1,'c')
    print "D", data,

R1, R2 = routine1('x'), routine2()
(current, data), _ = R1.next(), R2.next()

while True:
    try:current, data = current.send(data)
    except StopIteration: break 
