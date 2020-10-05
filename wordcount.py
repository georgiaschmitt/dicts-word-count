def count_words(filename):
    """Return dictionary of word counts in the passed file."""
    file_to_count = open(filename)
    word_counts = {}
    for line in file_to_count:
        line = line.rstrip()
        words = line.split(" ")
        words = [word.lower() for word in words]
        for word in words:
            if word[-1] in (",", ".", "?"):
                word = word[:-1]
            word_counts[word] = word_counts.get(word, 0) + 1

    for word, count in word_counts.items():
        print(word, count)

count_words("test.txt")
count_words("twain.txt")