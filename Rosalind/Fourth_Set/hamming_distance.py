#Rufino Salgado
#CS 327-1
import os

def main():
    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'hamming.txt'
    f = open(path, 'r')
    strings = f.readlines()
    f.close()
    seq_one = strings[0]
    seq_two = strings[1]

    miss = 0
    for i in range(0, len(seq_two)):
        #print(i)
        if seq_one[i] != seq_two[i]:
            miss+=1

    path = os.environ['PYTHONPATH'] + os.path.sep + 'files' + os.path.sep + 'hamming_output.txt'
    f = open(path, 'w')
    f.write(str(miss))
    f.close()

    print('Done')

if __name__ == '__main__':
    main()