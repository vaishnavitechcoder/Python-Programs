import string
def find_frequency(sentence):
    str1=[]
    from collections import Counter
    for i in sentence.split(' '):
        str1 = count(i) in sentence
    return ' '.join(map(str,str1))