def routine():
    print "A"; yield CR2
    print "B"; yield CR2

def routine2():
    print "C"; yield CR1
    print "D"; yield "DONE"


CR1, CR2  = routine(), routine2()
current = CR1


while True:
    if current is "DONE": break
    current = current.next()
