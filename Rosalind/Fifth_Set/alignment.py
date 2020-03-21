#Rufino Salgado
#CS 327 Spring 2020

import os
import numpy as np

def main():
    file = 'alignment.txt'
    blosum_file = 'blosum.txt'
    strings = intake(file)
    b_strings = intake(blosum_file)
    #print(b_strings)
    print(strings)
    seq_one = strings[0]
    seq_two = strings[1]
    blosum62 = "ACDEFGHIKLMNPQRSTVWY"
    alpha = 5
    score = 0

    len_one = len(seq_one)
    len_two = len(seq_two)
    len_blosum62 = len(blosum62)

    score_matrix = np.zeros((len_one+1, len_two+1), dtype=int)
    backtrack_matrix = np.zeros((len_one+1, len_two+1), dtype=int)
    blosum62_matrix = import_blosum(b_strings, len_blosum62)

    load_matrices(alpha, backtrack_matrix, blosum62, blosum62_matrix, len_one, len_two, score_matrix, seq_one, seq_two)

    score, lcs1, lcs2 = find_lcs(backtrack_matrix, score_matrix, len_one, len_two, seq_one, seq_two, score)

    print(score_matrix)
    print(backtrack_matrix)
    #print(blosum62_matrix)
    print(score)
    print(lcs1)
    print(lcs2)

    output_file = 'alignment_output.txt'
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + output_file
    f = open(path, 'w')
    f.write(str(score) + '\n')
    f.write(str(lcs2) + '\n')
    f.write(lcs1)
    f.close()


def find_lcs(backtrack_matrix, score_matrix, len_one, len_two, seq_one, seq_two, score):
    lcs1 = ''
    lcs2 = ''
    print("len_one: " + str(len_one))
    print("len_two: " + str(len_two))
    print('score: ' + str(score_matrix[len_one][len_two]))
    score += score_matrix[len_one][len_two]
    while len_one > 0 or len_two > 0:
        print(seq_one[len_one-1] +' ' + seq_two[len_two-1])
        if backtrack_matrix[len_one][len_two] == 1 or len_two == 0:
            lcs1 += '-'
            lcs2 += seq_one[len_one-1]
            len_one -= 1
            print('up')
        elif backtrack_matrix[len_one][len_two] == -1 or len_one == 0:
            lcs2 += '-'
            lcs1 += seq_two[len_two-1]
            len_two -= 1
            print('left')
        else:
            #if backtrack_matrix[len_one][len_two] == 0 and seq_one[len_one - 1] == seq_two[len_two - 1]:
            #print( seq_one[len_one])
            lcs1 += seq_two[len_two-1]
            lcs2 += seq_one[len_one-1]
            len_one -= 1
            len_two -= 1
            print('diag')
        print("len_one: " + str(len_one))
        print("len_two: " + str(len_two))


    lcs1 = lcs1[::-1]
    lcs2 = lcs2[::-1]
    print(lcs1)
    print(lcs2)
    return score, lcs1, lcs2

def load_matrices(alpha, backtrack_matrix, blosum62, blosum62_matrix, len_one, len_two, score_matrix, seq_one, seq_two):
    for i in range(0, len_two + 1):
        if i == 0:
            for j in range(1, len_one + 1):
                score_matrix[j][i] = score_matrix[j - 1][i] - alpha
            for j in range(1, len_two + 1):
                score_matrix[i][j] = score_matrix[i][j - 1] - alpha
    for i in range(1, len_one + 1):
        for j in range(1, len_two + 1):
            v = blosum62.index(seq_one[i - 1])
            w = blosum62.index(seq_two[j - 1])
            #print('row: ' + str(seq_one[i - 1]))
            #print('col: ' + str(seq_two[j - 1]))
            #print(str(v) + ' ' + str(w))
            tempDown = score_matrix[i - 1][j] - alpha
            tempRight = score_matrix[i][j - 1] - alpha
            tempDiag = score_matrix[i - 1][j - 1] + blosum62_matrix[v][w]
            #print('down: ' + str(tempDown))
            #print('right ' + str(tempRight))
            #print('diag: ' + str(tempDiag))
            m = max(tempDown, tempRight, tempDiag)
            score_matrix[i][j] = m
            t = 0
            if m == tempDown:
                t = 1
                #print('down')
            elif m == tempRight:
                t = -1
                #print('right')
            else:
                t = 2
                #print('diag')
            backtrack_matrix[i][j] = t


def import_blosum(b_strings, len_blosum62):
    blosum62_matrix = np.zeros((len_blosum62, len_blosum62), dtype=int)
    for b in range(0, len_blosum62):
        line = b_strings[b].replace('  ', ' ').split(' ')
        # print(line)
        for i in range(0, len_blosum62):
            blosum62_matrix[b][i] = int(line[i])
    return blosum62_matrix


def intake(file):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + file
    f = open(path, 'r')
    strings = f.readlines()
    f.close()
    strings = [s.rstrip('\n') for s in strings]
    return strings


if __name__ == '__main__':
    main()

'''
[[ 4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2]
 [ 0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2]
 [-2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3]
 [-1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2]
 [-2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3]
 [ 0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3]
 [-2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2]
 [-1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1]
 [-1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2]
 [-1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1]
 [-1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1]
 [-2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2]
 [-1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3]
 [-1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1]
 [-1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2]
 [ 1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2]
 [ 0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2]
 [ 0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1]
 [-3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2]
 [-2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7]]
'''