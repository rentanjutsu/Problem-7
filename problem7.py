wordList = []
tweet = input()
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
# wordList.append(word)
        word = ''
if stAdd:
    wordList.append(word)

print(wordList)
