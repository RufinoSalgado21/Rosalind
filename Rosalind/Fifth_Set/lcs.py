#Rufino Salgado
#CS 327 Spring 2020

import os
import numpy as np

def main():
    strings = intake('lcs.txt')
    print(strings)
    seq_one = strings[0]
    seq_two = strings[1]
    len_one = len(seq_one)
    len_two = len(seq_two)
    score_matrix = np.zeros((len_one+1, len_two+1), dtype=int)
    backtrack_matrix = np.zeros((len(seq_one)+1, len(seq_two)+1), dtype=int)
    #print(score_matrix)
    #print(backtrack_matrix)

    fill_matrices(backtrack_matrix, len_one, len_two, score_matrix, seq_one, seq_two)
    lcs = find_lcs(backtrack_matrix, len_one, len_two, seq_one, seq_two)
    print(score_matrix)
    print(backtrack_matrix)
    print('LCS: ' + lcs)

    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'lcs_output.txt'
    f = open(path, 'w')
    f.write(lcs)
    f.close()


def find_lcs(backtrack_matrix, len_one, len_two, seq_one, seq_two):
    lcs = ''
    while len_one > 0 and len_two > 0:
        print(seq_one[len_one-1] +' ' + seq_two[len_two-1])
        if backtrack_matrix[len_one][len_two] == 1:
            len_one -= 1
            print('up')
        elif backtrack_matrix[len_one][len_two] == -1:
            len_two -= 1
            print('left')
        else:
            #if backtrack_matrix[len_one][len_two] == 0 and seq_one[len_one - 1] == seq_two[len_two - 1]:
            #print( seq_one[len_one])
            lcs += seq_one[len_one-1]
            len_one -= 1
            len_two -= 1
            print('diag')
    lcs = lcs[::-1]
    return lcs


def fill_matrices(backtrack_matrix, len_one, len_two, score_matrix, seq_one, seq_two):
    for i in range(1, len_one + 1):
        for j in range(1, len_two + 1):
            tempDown = score_matrix[i - 1][j]
            tempRight = score_matrix[i][j - 1]
            tempDiag = score_matrix[i - 1][j - 1]
            if seq_one[i - 1] == seq_two[j - 1]:
                #print(seq_one[i-1] + ' ' + seq_two[j-1] + str(i) + ',' + str(j))
                tempDiag += 1
            # print('down: ' + str(tempDown) + ' right: ' + str(tempRight) + ' diag: ' +
            m = max(tempDown, tempRight, tempDiag)
            t = 2
            score_matrix[i][j] = m
            if m == tempDown:
                t = 1
            elif m == tempRight:
                t = -1
            else:
                t = 2
            backtrack_matrix[i][j] = t


def intake(file):
    path = os.environ['PYTHONPATH'] + os.path.sep + "files" + os.path.sep + file
    f = open(path, 'r')
    strings = f.readlines()
    strings = [s.rstrip('\n') for s in strings]
    return strings


if __name__ == '__main__':
    main()


'''
    for i in range(1, len_one + 1):
        for j in range(1, len_two + 1):
            i_txt = 'i: ' + str(i)
            j_txt = 'j: ' + str(j)
            ltr_txt = seq_one[i - 1] + ',' + seq_two[j - 1]
            print(i_txt + ' ' + j_txt + ' ' + ltr_txt)
'''


'''
    i: 1 j: 1 A,A
i: 1 j: 2 A,C
i: 1 j: 3 A,A
i: 1 j: 4 A,C
i: 1 j: 5 A,T
i: 1 j: 6 A,G
i: 1 j: 7 A,T
i: 1 j: 8 A,G
i: 1 j: 9 A,A
i: 2 j: 1 A,A
i: 2 j: 2 A,C
i: 2 j: 3 A,A
i: 2 j: 4 A,C
i: 2 j: 5 A,T
i: 2 j: 6 A,G
i: 2 j: 7 A,T
i: 2 j: 8 A,G
i: 2 j: 9 A,A
i: 3 j: 1 C,A
i: 3 j: 2 C,C
i: 3 j: 3 C,A
i: 3 j: 4 C,C
i: 3 j: 5 C,T
i: 3 j: 6 C,G
i: 3 j: 7 C,T
i: 3 j: 8 C,G
i: 3 j: 9 C,A
i: 4 j: 1 C,A
i: 4 j: 2 C,C
i: 4 j: 3 C,A
i: 4 j: 4 C,C
i: 4 j: 5 C,T
i: 4 j: 6 C,G
i: 4 j: 7 C,T
i: 4 j: 8 C,G
i: 4 j: 9 C,A
i: 5 j: 1 T,A
i: 5 j: 2 T,C
i: 5 j: 3 T,A
i: 5 j: 4 T,C
i: 5 j: 5 T,T
i: 5 j: 6 T,G
i: 5 j: 7 T,T
i: 5 j: 8 T,G
i: 5 j: 9 T,A
i: 6 j: 1 T,A
i: 6 j: 2 T,C
i: 6 j: 3 T,A
i: 6 j: 4 T,C
i: 6 j: 5 T,T
i: 6 j: 6 T,G
i: 6 j: 7 T,T
i: 6 j: 8 T,G
i: 6 j: 9 T,A
i: 7 j: 1 G,A
i: 7 j: 2 G,C
i: 7 j: 3 G,A
i: 7 j: 4 G,C
i: 7 j: 5 G,T
i: 7 j: 6 G,G
i: 7 j: 7 G,T
i: 7 j: 8 G,G
i: 7 j: 9 G,A
i: 8 j: 1 G,A
i: 8 j: 2 G,C
i: 8 j: 3 G,A
i: 8 j: 4 G,C
i: 8 j: 5 G,T
i: 8 j: 6 G,G
i: 8 j: 7 G,T
i: 8 j: 8 G,G
i: 8 j: 9 G,A
'''