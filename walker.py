
import os
import sys

def walk(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            #if os.path.isdir(file):
                #print "yeeeeeeeeeeees"
               # walk(os.path.abspath (file))
            #else:
                yield (os.path.join(root,file))


def helper(item,path):
    a = walk(path)
    for c in a:
        if os.path.split(c)[1] == item:
            yield c


print sys.path
