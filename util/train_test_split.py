import os, sys

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

for line in sys.stdin:
    line = line.strip()
    qid, docid, mark = line.split('\t')
    if (int(qid) % 10 < 2):
        errprint(line)
    else:
        print(line)
