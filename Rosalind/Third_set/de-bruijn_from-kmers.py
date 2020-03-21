#Rufino Salgado
#cs 327-1 Spring 2020

import os
from collections import defaultdict


def prefix(read):
    return read[0:len(read) - 1]


def suffix(read):
    return read[1:len(read)]


def prefixes(lst):
    prefix_lst = []
    for l in lst:
        prefix_lst.append(prefix(l))
    # print(prefix_lst)
    return prefix_lst


def suffixes(lst):
    suffix_lst = []
    for l in lst:
        suffix_lst.append(suffix(l))
    # print(suffix_lst)
    return suffix_lst

def print_dict(d):
    k = ''
    for key in d.keys():
        k = k + ' ['+ key + ' -> '
        for v in d[key]:
            k = k + v + ','
        k = k.rstrip(',')
        k += ']'
    print(k)

def output_dict(dict, output_file):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + output_file
    f = open(path, 'w')
    for index, key in enumerate(dict.keys()):
        pair = key + ' -> '
        for value in dict[key]:
            pair += value + ','
        pair = pair.rstrip(',')
        f.write(pair)
        if index != len(dict.keys())-1:
            f.write('\n')
    f.close()

def main():
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'de_bruijn_from_kmers.txt'
    f = open(path, 'r')
    lst = f.readlines()
    f.close()

    for index, l in enumerate(lst):
        lst[index] = l.rstrip('\n')

    lst.sort()
    d = defaultdict(list)

    pfx = prefixes(lst)
    sfx = suffixes(lst)
    for l in lst:
        #print(l)
        d[l] = []

    print_dict(d)
    for l in lst:
        p = prefix(l)
        s = suffix(l)
        matches = []
        for index,kmer in enumerate(pfx):
            if s == kmer and kmer not in matches:
                matches.append(lst[index])
        for m in matches:
            d[l].append(m)

    removes = []
    for k in d.keys():
        if len(d[k]) == 0:
            removes.append(k)
    for r in removes:
        d.pop(r, None)

    print_dict(d)

    output_dict(d,'de_bruijn_from_kmers_output.txt')


if __name__ == '__main__':
    main()
    '''
input
GAGG
CAGG
GGGG
GGGA
CAGG
AGGG
GGAG
['AGGG', 'CAGG', 'CAGG', 'GAGG', 'GGAG', 'GGGA', 'GGGG']

output
AGG -> GGG
CAG -> AGG,AGG
GAG -> AGG
GGA -> GAG
GGG -> GGA,GGG
    '''