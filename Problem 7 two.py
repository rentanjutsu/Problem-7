running = True
num = int(input())
wordList = []

while running:
    # This is so that the program knows how many tweets exist
    for line in range(num):
        tweet = input("Input Tweets Here:")
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
        if stAdd:
            wordList.append(word)

    print(wordList)
