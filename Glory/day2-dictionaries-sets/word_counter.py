text = "python is great and python is fun and python is easy"
word_list = text.split()
word_frequencies = {}
for word in word_list:
    word_frequencies[word] = word_frequencies.get(word, 0) + 1
# most frequent word count
most_frequent = max(word_frequencies)
#print(word_frequencies)
print(most_frequent)
