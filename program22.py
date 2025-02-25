def frequency(input):
    freq = {}

    for word in input.split():
        freq[word] = freq.get(word, 0) + 1

    words = list(freq.keys())
    words.sort()

    for w in words:
        print(f'{w}:{freq[w]}')

frequency('New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.')