import string
import itertools

def test(seqs):
    pos = 0
    neg = 0
    for alpha in seqs:
        if alpha in corpus:
            pos += 1
        else:
            neg += 1
    print "positive: ", pos
    print "negative: ", neg
    return pos, neg

if __name__ == "__main__":
    corpus = ""
    with open("corpus.txt", "r") as corpus_file:
        corpus = corpus_file.read().lower()
    order1 = list(string.ascii_lowercase)
    order2 = map("".join, itertools.product(order1, repeat=2))
    order3 = map("".join, itertools.product(order1, repeat=3))
    #test(order1)
    #test(order2)
    test(order3)
