#Rufino Salgado
#CS 327 Spring 2020
import os
import numpy as np

def main():
    #print

    #intake file
    cols, lst, nums, rows = intake()

    nums = filter(cols, lst, rows)

    #get first two numbers as total row and col
    num_of_cols, num_of_rows = format_tales(cols, nums, rows)

    matrix = np.zeros((num_of_cols+1, num_of_rows+1), dtype=int)

    load_initial_edges(cols, matrix, num_of_cols, num_of_rows, rows)

    load_remaining_matrix_values(cols, matrix, num_of_cols, num_of_rows, rows)

    print(matrix)
    print(rows)
    print(cols)

    len = str(matrix[num_of_cols][num_of_rows])
    output_longest_path(len)


def output_longest_path(len):
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'manhattan_longest_len_output.txt'
    f = open(path, 'w')
    f.write(len)
    f.close()


def load_remaining_matrix_values(cols, matrix, num_of_cols, num_of_rows, rows):
    # go through each remaining node starting with 1,1.
    # enter max of previous nodes + edges
    for i in range(1, num_of_cols + 1):
        for j in range(1, num_of_rows + 1):
            m1 = int(matrix[i - 1][j]) + int(cols[i - 1][j])
            m2 = int(matrix[i][j - 1]) + int(rows[i][j - 1])
            matrix[i][j] = max(m1, m2)


def load_initial_edges(cols, matrix, num_of_cols, num_of_rows, rows):
    # load matrix first row
    for r in range(1, num_of_rows + 1):
        r = int(r)
        matrix[0][r] = int(matrix[0][r - 1]) + int(rows[0][r - 1])
    print(matrix)
    # load matrix  first col
    for c in range(1, num_of_cols + 1):
        c = int(c)
        matrix[c][0] = int(matrix[c - 1][0]) + int(cols[c - 1][0])
    print(matrix)


def format_tales(cols, nums, rows):
    num_of_cols = int(nums[0])
    num_of_rows = int(nums[1])
    print(num_of_rows)
    print(num_of_cols)
    for index, row in enumerate(rows):
        rows[index] = row.split(' ')
    for index, col in enumerate(cols):
        cols[index] = col.split(' ')
    print(rows)
    print(cols)
    return num_of_cols, num_of_rows


def filter(cols, lst, rows):
    reading_rows = True
    for index, l in enumerate(lst):
        # lst[index] = l.rstrip('\n')
        if index == 0:
            nums = l.rstrip('\n')
            nums = nums.split(' ')
        elif l == "-\n":
            reading_rows = False
        elif reading_rows:
            cols.append(l.rstrip('\n'))
        else:
            rows.append(l.rstrip('\n'))
    return nums


def intake():
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'manhattan_longest_len.txt'
    f = open(path, 'r')
    lst = f.readlines()
    nums = ''
    rows = []
    cols = []
    f.close()
    return cols, lst, nums, rows


if __name__ == '__main__':
    main()