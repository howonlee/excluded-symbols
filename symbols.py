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

def seq_to_idx(seq):
    """
    sequence to the index which we will index into the matrix with
    """
    pass

def display(seqs, order=2):
    #extend this for arbitrary order > 1
    dims = (26 ** (order - 1), 26 ** (order - 1))
    seq_mat = np.zeros(dims)
    for seq in seqs:
        seq_mat[seq_to_order(seq)] += 1
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
