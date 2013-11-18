import random
NUM = 12
#massive = [random.randint(0,NUM) for c in range(NUM)]
massive = [-1,2,3]
a = massive[0]
for c in massive:
    if a < c:
        a = c

print massive
print max(massive)
print a


d = f = massive[0]
for c in massive:
    if d <= c:
        f = d
        d = c
    else:
        if f < c:
            f = c
print f,d 
