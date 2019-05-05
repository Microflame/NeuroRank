import sys
import numpy as np

df_dict = {}

model_path = sys.argv[1]
with open(model_path) as f:
    for line in f:
        w, df = line.split()
        df_dict[w] = int(df)

total_docs_num = df_dict['TOTAL_DOCS']

for line in sys.stdin:
    query, title = line.split('\t')
    query = query.split()
    title = title.split()
    score = 0.0
    for w in query:
        if w in title:
            score += np.log(total_docs_num / df_dict.get(w, 1.0))
    print(score)
