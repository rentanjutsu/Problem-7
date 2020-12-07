from collections import Counter

num = int(input())
wordList = []
for line in range(num):
    tweet = input().lower()
    blankLine = input()

    words = [word[1:] for word in tweet.strip().split(" ") if word[0] == '#']
    wordList.extend(words)

col = Counter(wordList)

for key, val in col.most_common():
    print(str(key) + " " + str(val))

# numList = [i for i in range(100)]
# key, value = [1, 2]