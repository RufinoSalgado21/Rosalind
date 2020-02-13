#Rufino Salgado
#cs-327-1 spring 2020
import os


def find_mrna(rna):
    rosetta = {'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V',
               'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
               'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V',
               'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
               'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A',
               'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
               'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A',
               'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
               'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D',
               'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
               'UAA': 'Stop', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E',
               'UAG': 'Stop', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
               'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G',
               'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
               'UGA': 'Stop', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G',
               'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'}
    mrna = ''
    if rna in rosetta.keys():
        mrna = rosetta[rna]
    return mrna


def break_into_triples(path):
    f = open(path, 'r')
    s = f.readlines()
    #print('s ')
    #print(s)
    seq = s[0][0:len(s[0])]
    threes = []
    index = 0
    while index < int(len(seq)):
        threes.append(seq[index:index+3])
        index+=3
    f.close()
    #print(threes)
    return threes


def construct_codon(rna):
    codon = ''
    for r in rna:
        #print(r)
        c = find_mrna(r)
        if c == 'Stop':
            return codon
        codon += c
        #print(codon)
    return codon


if __name__ == '__main__':
    path = os.environ['PYTHONPATH'] + os.path.sep + 'Files' + os.path.sep + 'rna.txt'
    rna = break_into_triples(path)
    print(rna)
    codon = construct_codon(rna)
    print(codon)
