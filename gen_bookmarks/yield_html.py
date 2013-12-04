#coding: utf-8

import time


#my bookmarks from google chrome
FILE = "bookmarks.html"

def file_gen(name):
    filename  = open(name)
    lines     = (line.strip() for line in filename)
    mod_lines = (line[12:] for line in lines if
                 line.startswith("<DT><A HREF="))
    return mod_lines   

#first variant    
def file_gen2(name):
    f = open(name)
    for line in f:
        line = line.strip()
        if line.startswith("<DT><A HREF="):
            yield line[12:]
#gen value       
def worker_value():
    print "Worker1 start"
    s = ''
    while True:
        line = yield s
        s = line.split('"', 2)[1]

#gen key 
def worker_key():
    print "Worker2 start"
    s = ''
    while True:
        line = yield s
        s = line[:-4].rsplit('>', 1)[1] or "non"
         
        
    
def make_dict(bookmarks):
    gen_lines = file_gen(bookmarks)
    workers = [worker_key(), worker_value()]
    for c in workers: c.next()
    d = dict((workers[0].send(c), workers[1].send(c))
            for c in gen_lines)
    return d 
        

if __name__ == "__main__":
    start = time.time()
    d = make_dict(FILE)
    print "EEEEEE", time.time()-start

        
        

    
