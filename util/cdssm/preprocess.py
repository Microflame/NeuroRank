import sys
import numpy as np

N = 3
nuw_words = 30
num_ngrams = 20
ngrams_file = sys.argv[1]
ngrams = {}

def word2ngrams(word):
    w = '#' + word + '#'
    for i in range(len(w) - N + 1):
        yield w[i:i+N]

def process_phrase(phrase):
    ngram_ids = np.full([nuw_words, num_ngrams], 0)
    for word_idx, word in enumerate(phrase.split()[:nuw_words]):
        for ngram_idx, ngram in enumerate(list(word2ngrams(word))[:num_ngrams]):
            ngram_id = ngrams.get(ngram, 0)
            ngram_ids[word_idx, ngram_idx] = ngram_id
    return ngram_ids.ravel()

i = 1
with open(ngrams_file) as f:
    for line in f:
        ngrams[line.strip()] = i
        i += 1

for line in sys.stdin:
    mark, query, doc = line.split('\t')
    query_ids = map(str, process_phrase(query))
    doc_ids = map(str, process_phrase(doc))
    result = '\t'.join(query_ids) + '\t' + '\t'.join(doc_ids)
    print(result)
