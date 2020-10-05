import sys

def count_words():
    """Return dictionary of word counts in the passed file."""
    
    word_counts = {}
    filename = sys.argv[1]

    for line in open(filename):
        line = line.rstrip()
        words = line.split(" ")
        words = [word.lower() for word in words]
        for word in words:
            word = word.strip(''''/",.!?-#$%^&();:_''')
            word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in sorted(word_counts.items()):
        print(word, count)


count_words()




