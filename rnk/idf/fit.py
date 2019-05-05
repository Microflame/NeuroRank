import sys
from collections import defaultdict

df_dict = defaultdict(int)

for line in sys.stdin:
    mark, query, doc = line.split('\t')
    words = set(doc.split())
    df_dict['TOTAL_DOCS'] += 1
    for w in words:
        df_dict[w] += 1

for w, df in df_dict.items():
    print('%s\t%d' % (w, df))
