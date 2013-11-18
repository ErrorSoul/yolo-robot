import random
def randomwalk_list():
    last, rand = 1, random.random()
    nums = []
    while rand > 0.1:
        if abs (last - rand) >= 0.4:
            last = rand
            nums.append(rand)
        else:
            print '*'
        rand = random.random()
    nums.append(rand)
    return nums

for num in randomwalk_list():
    print num

def mul_table():
    print "{0}   {1}".format("X", "   ".join([str(c) for c in range(1,10)]))
    l = [[str(c * a) for c in range(1,10)] for a in range(1,10)]
    for k,c in enumerate(l):
        print "{0}   {1: <}".format(k +1, "   ".join(c))
print mul_table()
import sys, time

threads = []
TOTALSWITCHES = 10**6
NUMTHREADS    = 10**5

def null_factory():
    def empty():
        while 1: yield None
    return empty()

def quitter():
    for n in xrange(TOTALSWITCHES/NUMTHREADS):
        yield None

def scheduler():
    global threads
    try:
        while 1:
            for thread in threads: thread.next()
    except StopIteration:
        pass

if __name__ == "__main__":
    for i in range(NUMTHREADS):
        threads.append(null_factory())
    threads.append(quitter())
    starttime = time.clock()
    scheduler()
    print "TOTAL TIME:    ", time.clock()-starttime
    print "TOTAL SWITCHES:", TOTALSWITCHES
    print "TOTAL THREADS: ", NUMTHREADS
