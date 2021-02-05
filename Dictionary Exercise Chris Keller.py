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

"""
PART TWO OF ASSIGNMENT
"""

ws_file = open("WorldSeriesWinners.txt", "r")

ws_dict = {}

num_wins = {}

for i in range(1903, 2009):
    if i != 1904 and i != 1994:
        team = ws_file.readline().rstrip("\n")
        ws_dict[i] = team


for team in ws_dict.values():
    if team in num_wins:
        num_wins[team] += 1
    else:
        num_wins[team] = 1


year = int(
    input(
        "Pick a year between 1903 and 2008, and I'll tell you who won that World Series. "
    )
)

if year in [1904, 1994]:
    print("Sorry, the World Series was not played in 1904 or 1994.")
else:
    print("The " + ws_dict[year] + " won the World Series that year.")
    team = ws_dict[year]
    print("They have won the world series " + str(num_wins[team]) + " times.")

ws_file.close()
