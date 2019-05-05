import sys
import numpy as np

def calc_dcg(m, p, k=5):
    assert len(m) == len(p)
    order = np.argsort(-p)[:k]
    dcg = 0
    for i in order:
        dcg += (2 ** m[i] - 1) / (np.log2(i + 2))
    return dcg

marks_file = sys.argv[1]
marks = np.loadtxt(marks_file)

preds_file = sys.argv[2]
preds = np.loadtxt(preds_file)

groups_file = sys.argv[3]
groups = np.loadtxt(groups_file)

assert marks.shape == preds.shape
assert marks.shape == groups.shape

ndcgs = []

start = 0
cur_group = groups[0]
for i in range(len(marks)):
    if groups[i] != cur_group:
        m = marks[start:i]
        p = preds[start:i]
        ndcg = calc_dcg(m, p) / (calc_dcg(m, m) + 1e-5)
        ndcgs.append(ndcg)
        start = i
        cur_group = groups[i]
m = marks[start:]
p = preds[start:]
ndcg = calc_dcg(m, p) / (calc_dcg(m, m) + 1e-5)
ndcgs.append(ndcg)

print(np.mean(ndcgs))
