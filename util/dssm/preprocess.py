import sys
import numpy as np

N = 3
num_ngrams_in_phrase = 100
ngrams_file = sys.argv[1]
ngrams = {}

def word2ngrams(word):
    w = '#' + word + '#'
    for i in range(len(w) - N + 1):
        yield w[i:i+N]

def process_phrase(phrase):
    phrase_ids = ['0'] * num_ngrams_in_phrase
    i = 0
    for word in phrase.split():
        for ngram in word2ngrams(word):
            ngram_id = ngrams.get(ngram, 0)
            phrase_ids[i] = str(ngram_id)
            i += 1
            if i == num_ngrams_in_phrase:
                return phrase_ids
    return phrase_ids

i = 1
with open(ngrams_file) as f:
    for line in f:
        ngrams[line.strip()] = i
        i += 1

for line in sys.stdin:
    mark, query, doc = line.split('\t')
    query_ids = process_phrase(query)
    doc_ids = process_phrase(doc)
    result = '\t'.join(query_ids) + '\t' + '\t'.join(doc_ids)
    print(result)
