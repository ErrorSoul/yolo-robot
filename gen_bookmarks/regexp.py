import re
from yield_html import FILE

def file_gen(f):
    filename = open(f)
    for line in filename:
        yield line

        

exp = re.compile(r"""<DT><A HREF="(?P<source>.+)"\s+ADD_DATE.+>(?P<q>.+)(?=</A>)""")

gen = file_gen(FILE)

for c in gen:
    if  exp.search(c) is not None:
        print exp.search(c).group()
## h = ""
## for c in gen:
##     h += c

## for c in re.finditer(exp, h):
##     print c.group('source')

## for a, c in enumerate(gen):
##     print a, re.findall(exp, c)
