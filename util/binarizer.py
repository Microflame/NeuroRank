import os, sys

for line in sys.stdin:
    line = line.strip()
    query, doc, mark = line.split('\t')
    mark = int(mark)
    if mark >= 3:
        print('1\t%s\t%s' % (query, doc))
    else:
        print('0\t%s\t%s' % (query, doc))
