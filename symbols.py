import string
import itertools
import numpy as np
import matplotlib.pyplot as plt

def test(seqs):
    pos = 0
    pos_seqs = []
    neg = 0
    neg_seqs = []
    for alpha in seqs:
        if alpha in corpus:
            pos += 1
            pos_seqs.append(alpha)
        else:
            neg += 1
            neg_seqs.append(alpha)
    print "positive: ", pos
    print "negative: ", neg
    return pos_seqs, neg_seqs

def ctoi(char):
    return ord(char) - 97

def display(seqs):
    seq_mat = np.zeros((26,26))
    for alpha in seqs:
        seq_mat[ctoi(alpha[0]), ctoi(alpha[1])] += 1
    plt.matshow(seq_mat)
    plt.show()

if __name__ == "__main__":
    corpus = ""
    with open("corpus.txt", "r") as corpus_file:
        corpus = corpus_file.read().lower()
    order1 = list(string.ascii_lowercase)
    order2 = map("".join, itertools.product(order1, repeat=2))
    order3 = map("".join, itertools.product(order1, repeat=3))
    #test(order1)
    pos, neg = test(order2)
    display(neg)
