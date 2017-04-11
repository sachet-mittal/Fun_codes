from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from collections import defaultdict
from heapq import nlargest
import os

def summarize(text, n):
    sents = sent_tokenize(text)
    assert n <= len(sents)
    word_sent = word_tokenize(text.lower())
    _stopwords = set(stopwords.words("english") + list(punctuation))

    word_sent = [word for word in word_sent if word not in _stopwords]

    freq = FreqDist(word_sent)

    ranking = defaultdict(int)

    for i, sent in enumerate(sents):
        for w in word_tokenize(sent.lower()):
            if w in freq:
                ranking[i] += freq[w]

    sents_idx = nlargest(n, ranking, key=ranking.get)
    return [sents[j] for j in sorted(sents_idx)]


if __name__ == "__main__":
    with open(os.path.join(os.path.split(__file__)[0], 'data.txt')) as f:
        data = f.read()
        data = unicode(data, 'utf-8')
        data = data.encode('ascii', errors="replace").replace("?", " ")
        print "\n".join(summarize(data, 3))
