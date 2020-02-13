#Rufino Salgado
#CS 327-1 Spring 2020
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


def break_into_triples(seq):
    threes = []
    index = 0
    while index < int(len(seq)):
        threes.append(seq[index:index+3])
        index+=3
    return threes


def intake(path):
    f = open(path, 'r')
    s = f.readlines()
    f.close()
    s = s[1:]
    #print(s)
    s2 = ''
    for seq in s:
        #print(seq)
        seq = seq.rstrip('\n')
        s2 += seq
    #print(s2)
    return s2


def construct_codon(rna):
    codon = []
    frame = 0
    seq = ''
    for r in rna:
        c = find_mrna(r)
        if c == 'Stop':
            codon.append(seq)
            seq = ''
            frame += 1
        seq += c
    return codon

def transcribe(dna):
    transcription = ''
    for c in dna:
        if c == 'T':
            transcription += 'U'
        else:
            transcription += c
    return transcription

def split_into_codons(rna):
    searching = False
    codons = []
    index = 0
    temp = 0
    while index < len(rna)-3:
        if rna[index:index+3] == 'AUG':
            temp = index
            index += 3
            searching = True
            exit = ['UAG','UGA','UAA']
            while index < len(rna)-3 and searching:
                #print(rna[index:index+3])
                #print(codons)
                if rna[index:index+3] in exit:
                    codons.append(rna[temp:index+3])
                    index += 3
                    searching = False
                elif rna[index:index+3] == 'AUG'  :
                    print('rna' + rna[index:])
                    c = split_into_codons(rna[temp+3:])
                    print('c')
                    print(c)
                    index+=3
                    if(len(c) > 0):
                        for k in c:
                            if k not in codons:
                                codons.append(k)
                else:
                    index += 3
        else:
            index += 3
    return codons

def reverse_complement(rna):
    reverse_rna = ''
    reverse = {'A':'U','U':'A','C':'G','G':'C'}
    for r in rna:
        reverse_rna += reverse[r]
    return reverse_rna[::-1]


def find_codon(mrna, codon):
    global i, m, c
    for i in mrna:
        m = break_into_triples(i)
        c = construct_codon(m)
        if c not in codon:
            codon.append(c)
        #print(codon)


def write_to_file(codon, file_name):
    global path, c
    path = os.environ['PYTHONPATH'] + os.path.sep + 'Files' + os.path.sep + file_name
    f = open(path, 'w')
    for c in codon:
        f.write(c[0] + '\n')
    f.close()

def find(rna):
    mrna_1 = split_into_codons(rna)
    mrna_2 = split_into_codons(rna[1:])
    mrna_3 = split_into_codons(rna[2:])
    codon = []
    find_codon(mrna_1, codon)
    find_codon(mrna_2, codon)
    find_codon(mrna_3, codon)
    # complements
    reverse_rna = reverse_complement(rna)
    reverse_mrna = split_into_codons(reverse_rna)
    reverse_mrna_2 = split_into_codons(reverse_rna[1:])
    reverse_mrna_3 = split_into_codons(reverse_rna[2:])

    find_codon(reverse_mrna, codon)
    find_codon(reverse_mrna_2, codon)
    find_codon(reverse_mrna_3, codon)
    return codon

if __name__ == '__main__':
    path = os.environ['PYTHONPATH'] + os.path.sep + 'Files' + os.path.sep + 'openframes.txt'
    dna = intake(path)
    rna = transcribe(dna)
    output = []
    print(rna)
    output = find(rna)
    print(output)
    write_to_file(output, 'openframes_output.txt')
    '''
    mrna_1 = split_into_codons(rna)
    mrna_2 = split_into_codons(rna[1:])
    mrna_3 = split_into_codons(rna[2:])
    codon = []
    find_codon(mrna_1, codon)
    find_codon(mrna_2, codon)
    find_codon(mrna_3, codon)

    #complements
    reverse_rna = reverse_complement(rna)
    reverse_mrna = split_into_codons(reverse_rna)
    reverse_mrna_2 = split_into_codons(reverse_rna[1:])
    reverse_mrna_3 = split_into_codons(reverse_rna[2:])

    find_codon(reverse_mrna, codon)
    find_codon(reverse_mrna_2, codon)
    find_codon(reverse_mrna_3, codon)

    write_to_file(codon, 'openframes_output.txt')
    '''