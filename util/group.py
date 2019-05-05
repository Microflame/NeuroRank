import sys

prev_query = 0
group = 0

for line in sys.stdin:
    mark, query, doc = line.split('\t')
    if prev_query == 0:
        prev_query = query
    if query != prev_query:
        prev_query = query
        group += 1
    print(group)
