#Rufino Salgado
#CS 327-1 Spring
import os
from _collections import defaultdict
from random import randint


def main():
    dict = defaultdict(list)

    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'euler.txt'
    f = open(path, 'r')
    lst = f.readlines()
    f.close()

    for index, l in enumerate(lst):
        l = l.rstrip('\n')
        lst[index] = l.split(' -> ')
    #print(lst)

    for index, l in enumerate(lst):
        lst[index][1] = l[1].split(',')
    #print(lst)

    for l in lst:
        dict[l[0]] = l[1]
    #print(dict)

    num_of_edges = 0
    for v in dict.values():
        num_of_edges += len(v)

    r = str(randint(0,len(lst)-1))

    #print(r)
    euler = [r]
    #print(euler)
    more_to_do = True

    euler = find_cycle(dict, more_to_do, r)
    edges_used = len(euler)
    '''
    print(euler)
    print('edges: ' + str(num_of_edges))
    print('edges_used: ' + str(edges_used))
    '''
    while num_of_edges > edges_used:
        #print('searching new cycles...')
        more_to_do = True
        #print(r)
        while True:
            r = str(randint(0,len(lst)-1))
            #print('r ' + r, end=" ")
            if r in euler and len(dict[r]) > 0:
                #print('r ' + r)
                break
            #print(len(dict[str(r)]))

        #print('r ' +r)
        temp = r
        #print("temp: " + temp)
        new_cycle = find_cycle(dict, more_to_do, r)
        i = euler.index(temp)
        euler.pop(int(i))
        for index in range(len(new_cycle)):
            euler.insert(index + i, new_cycle[index])

        edges_used = len(euler)
        '''
        print(euler)
        print('edges: ' + str(num_of_edges))
        print('edges_used: ' + str(edges_used))
        '''
        path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'euler_output.txt'
        f = open(path, 'w')
        st = ''
        for s in euler:
            st = st + s + '->'
        st = st.rstrip('->')
        f.write(st)
        f.close()

def calc_used_edges(euler):
    #print('counting')
    finished = []
    for e in euler:
        if e not in finished:
            finished.append(e)
    edges_used = len(finished)
    return edges_used


def find_cycle(dict, more_to_do, r):
    #print('searching')
    euler = [r]
    while more_to_do:
        if len(dict[r]) == 0:
            more_to_do = False
        else:
            euler.append(dict[r][0])
            #print(euler)
            temp = r
            r = dict[r][0]
            #print(r)
            dict[temp].pop(0)
            #print(r)
    return euler


if __name__ == '__main__':
    print('searching...')
    main()
    print('Done')