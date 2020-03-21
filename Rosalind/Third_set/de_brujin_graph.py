#Rufino Salgado
#CS 327-1 Spring 2020

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
    for key in dict.keys():
        pair = key + ' -> '
        for value in dict[key]:
            pair += value + ','
        pair = pair.rstrip(',')
        f.write(pair + '\n')
    f.close()

def main():
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'de_bruijn_graph.txt'
    f = open(path, 'r')
    lst = f.readlines()
    f.close()
    for index, l in enumerate(lst):
        lst[index] = l.rstrip('\n')
    num = int(lst[0])
    txt = lst[1]

    composition = []
    length = len(txt) - num
    for index, r in enumerate(txt):
        if index <= length:
            composition.append(txt[index:index + num])
    composition.sort()
    #print(composition)

    d = defaultdict(list)
    #print_dict(d)

    pfx = prefixes(composition)
    sfx = suffixes(composition)
    '''
    print(pfx)
    print(sfx)
    '''
    for p in pfx:
        d[p] = []

    for p in pfx:
        #print('p: ' + p)
        for index, s in enumerate(sfx):
            #print('s: ' + s)
            if suffix(p) == prefix(s) and sfx[index] not in d[p]:
                #print(suffix(p) + ' ' + prefix(s))
                d[p].append(sfx[index])
    '''
    print(d.keys())
    print(d.values())
    '''
    print_dict(d)
    output_dict(d,'de_bruijn_graph_output.txt')



if __name__ == '__main__':
    main()
    '''
AAG -> AGA
AGA -> GAT
ATT -> TTC
CTA -> TAC
CTC -> TCT
GAT -> ATT
TCT -> CTA,CTC
TTC -> TCT
    '''