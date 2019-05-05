import os, sys

def errprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

queries_file = sys.argv[1]
queries = {}
with open(queries_file) as f:
    for line in f:
        qid, query = line.strip().split('\t')
        queries[int(qid)] = query.lower()


docs_file = sys.argv[2]
docs = {}
with open(docs_file) as f:
    for line in f:
        docid, title = line.split('\t')
        docs[int(docid)] = title.strip().lower()


err = 0
for line in sys.stdin:
    line = line.strip()
    qid, docid, mark = line.split('\t')
    query = queries.get(int(qid))
    title = docs.get(int(docid))
    if query is None or title is None:
        err += 1
        continue
    print('%s\t%s\t%s' % (query, title, mark))

errprint('Errors: %d' % err)
