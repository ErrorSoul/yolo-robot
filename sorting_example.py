from random import randint
from time import time

r = randint
N = 10000000

generator = ((r(1, N), r(1, N), r(1, N), r(1, N)) for c in range(N))


if __name__ == "__main__":
    start = time()
    ## for lst in sorted(generator):
    ##     print lst
    sorted(generator)
    end = time() - start
    print "Time {0}".format(end)
    
