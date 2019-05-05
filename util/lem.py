import sys

from pymystem3 import Mystem

m = Mystem()

for line in sys.stdin:
    mark, query, doc = line.split('\t')
    query = ''.join(m.lemmatize(query.strip())).strip().upper()
    doc = ''.join(m.lemmatize(doc.strip())).strip().upper()
    print('%s\t%s\t%s' % (mark, query, doc))
