#Rufino Salgado
#CS 327

import os

def main():
    num, lst = intake('kmer_composition.txt')
    total_lst = ''
    for l in lst:
        total_lst += l
    composition = []
    length = len(total_lst) - num
    for index, r in enumerate(total_lst):
        if index <= length:
            composition.append(total_lst[index:index+num])
    composition.sort()
    output_to_txt(composition)


def output_to_txt(output):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'kmer_composition_output.txt'
    out = open(path, 'w')
    for k in output:
        out.write(k + '\n')
    out.close()

def intake(name):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + name
    f = open(path, 'r')
    num = f.readline()
    lst = f.readlines()
    for index, l in enumerate(lst):
        lst[index] = l.rstrip('\n')
    f.close()
    return int(num), lst

if __name__ == '__main__':
    main()

