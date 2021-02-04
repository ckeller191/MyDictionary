"""
PART ONE OF ASSIGNMENT
"""

open_file = open("text.txt", "r")
string = ""

for line in open_file:
    string += line


undesired_punct = ["'", '"', ",", ".", "!", ":", ";", "#", "@", "-"]

no_punct = ""

for char in string:
    if char not in undesired_punct:
        no_punct = no_punct + char

word_count = {}


for word in no_punct.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_count.items()):
    print(f"{word:<12}{count}")

print("\nNumber of unique words: ", len(word_count))


open_file.close()