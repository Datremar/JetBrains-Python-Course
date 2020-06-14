from random import shuffle


print('H A N G M A N')

words = ['python', 'java', 'kotlin', 'javascript']

shuffle(words)

while True:

    play_trigger = input('Type "play" to play the game, "exit" to quit: ').lstrip('> ')

    if play_trigger == 'play':
        pass
    elif play_trigger == 'exit':
        break
    else:
        continue

    allowed_letters = 'qwertyuiopasdfghjklzxcvbnm'
    letters_set = set()

    word = '-' * len(words[0])

    letter = ' '
    tmp_word = ''
    lifes = 8

    while lifes > 0 and word != words[0]:
        letter = input(f'\n{word}\nInput a letter: ')

        letter.lstrip('> ')

        if len(letter) != 1:
            if letter == 'exit':
                exit(0)
            print('You should input a single letter')
            continue

        if letter not in allowed_letters:
            print('It is not an ASCII lowercase letter')
            continue

        if letter in letters_set:
            print('You already typed this letter')
            letters_set.add(letter)
            continue

        letters_set.add(letter)

        if letter in words[0] and letter not in word:
            word = list(word)
            for j in range(0, len(word)):
                if words[0][j] == letter:
                    word[j] = letter
            for char in word:
                tmp_word += char
            word = tmp_word
            tmp_word = ''
        else:
            print('No such letter in the word')
            lifes -= 1
    else:
        if word == words[0]:
            print('You guessed the word!\nYou survived!')
        else:
            print("You are hanged!")

    print()
