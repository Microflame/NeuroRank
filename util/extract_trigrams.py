import sys
from collections import defaultdict

N = 3
ngrams = defaultdict(int)

def word2ngrams(word):
    w = '#' + word + '#'
    for i in range(len(w) - N + 1):
        yield w[i:i+N]

for line in sys.stdin:
    words = line.split()[1:]
    for word in words:
        for ngram in word2ngrams(word):
            ngrams[ngram] += 1

for ngram, cnt in ngrams.items():
    if cnt > 10:
        print(ngram)
