
d  = (raw_input("Enter two numbers : ") for s in xrange(4))    
l  = (c.split(',')  for c in d )
l1 = (map(int,c) for c in l)
l2 = ( [range(1 + c[1]*n, 1 + c[1] + c[1]*n) for n in range(c[0])]  for c in l1)
## l2 = [(b[1], [list() for c in range(b[0])]) for b in l1]
## #l3 = (range(1 + ))
 
## for line  in l2:
##     k = 1
##     for lst in line[1]:
##         g = 0
##         while g < line[0]:
##             lst.append(k)
##             k+=1
##             g+=1


## for c in l2:
##     print c[1]
 


z = [range(1 + 3*n, 4 + 3*n) for n in range(3)]



