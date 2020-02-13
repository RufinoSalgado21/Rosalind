#Rufino Salgado
#CS 327

import os

def main():
    lst = intake('genome_reconstruct.txt')
    output = lst[0]
    for index, read in enumerate(lst):
        if index != 0:
            print(read[len(read)-1])
            output += read[len(read)-1]
    print(lst)
    print(output)
    output_to_txt(output)

def output_to_txt(output):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'genome_reconstruct_output.txt'
    out = open(path, 'w')
    out.write(output)
    out.close()

def intake(name):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + name
    f = open(path, 'r')
    lst = f.readlines()
    for index, l in enumerate(lst):
        lst[index] = l.rstrip('\n')
    #lst.sort()
    f.close()
    #print(lst)
    return lst

if __name__ == '__main__':
    main()

