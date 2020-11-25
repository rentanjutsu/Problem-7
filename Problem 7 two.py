num = int(input())
wordList = []

# This is so that the program knows how many tweets exist
for line in range(num):
    tweet = input()
    tweet = tweet.casefold()
# stAdd = start adding
    stAdd = False
    word = ''
    for letter in tweet:
        if letter == '#':
            stAdd = True
        if stAdd:
            word = word + letter
            print(word)
        if letter == ' ':
            stAdd = False
            wordList.append(word)
            word = ''
    else:
        continue
print(wordList)
