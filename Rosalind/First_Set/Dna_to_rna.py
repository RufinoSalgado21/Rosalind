#Rufino Salgado
#cs 327-1 Spring 2020
import os

def transcribe(dna):
    f = open(path, 'r')
    s = f.readlines()
    f.close()
    transcription = ''
    for c in s[0]:
        #print(c)
        if c == 'T':
            transcription += 'U'
        else:
            transcription += c
    return transcription

if __name__ == '__main__':
    path = os.environ['PYTHONPATH'] + os.path.sep + 'Files' + os.path.sep + 'rosalind_rna.txt'
    print(transcribe(path))