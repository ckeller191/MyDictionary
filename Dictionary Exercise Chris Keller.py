open_file = open("text.txt", "r")
string = ""

for line in open_file:
    string += line

word_count = {}


for word in string.split():
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1


print(f'{"WORD":<12}COUNT')

for word, count in sorted(word_count.items()):
    print(f"{word:<12}{count}")

print("\nNumber of unique words: ", len(word_count))


open_file.close()