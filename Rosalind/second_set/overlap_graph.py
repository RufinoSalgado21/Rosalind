#Rufino Salgado
#CS 327-1

#Spring 2020
import os
#['AGGCA', 'ATGCG', 'CATGC', 'GCATG', 'GGCAT']
def main():
    lst = intake('overlap_dataset.txt')
    prefix_lst = prefixes(lst)
    suffix_lst = suffixes(lst)
    #find leading read\
    overlap_graph = {}
    lead = ''
    lead = find_leading_kmer(lead, lst, overlap_graph, suffix_lst)
    #find next
    find_kmers(lead, lst, overlap_graph, prefix_lst)
    print(overlap_graph)
    output_to_txt(overlap_graph)


def output_to_txt(overlap_graph):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'overlap_graph_output.txt'
    output = open(path, 'w')
    for m in overlap_graph.keys():
        if overlap_graph[m] != '':
            output.write(m + ' -> ' + overlap_graph[m] + '\n')


def find_kmers(lead, lst, overlap_graph, prefix_lst):
    for l in lst:
        if prefix(l) != lead:
            next = ''
            for index, r in enumerate(prefix_lst):
                if r == suffix(l):
                    next = lst[index]
            overlap_graph[l] = next
        else:
            for index, r in enumerate(prefix_lst):
                if r == suffix(lead):
                    next = lst[index]
                    overlap_graph[lead] = lst[index]
                    break


def find_leading_kmer(lead, lst, overlap_graph, suffix_lst):
    for index, r in enumerate(lst):
        if prefix(r) not in suffix_lst:
            lead = lst[index]
            overlap_graph[lead] = ''
    return lead


def prefix(read):
    return read[0:len(read)-1]

def suffix(read):
    return read[1:len(read)]

def prefixes(lst):
    prefix_lst = []
    for l in lst:
        prefix_lst.append(prefix(l))
    #print(prefix_lst)
    return prefix_lst

def suffixes(lst):
    suffix_lst = []
    for l in lst:
        suffix_lst.append(suffix(l))
    #print(suffix_lst)
    return suffix_lst

def intake(name):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + name
    f = open(path, 'r')
    lst = f.readlines()
    for index, l in enumerate(lst):
        lst[index] = l.rstrip('\n')
    lst.sort()
    f.close()
    #print(lst)
    return lst


if __name__ == '__main__':
    main()