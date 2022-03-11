#Chapter 10 Scratch Pad

import random

def hangman(word):
    wrong = 0
    stages = ["",
             " _________      ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("Welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        guess = input(msg)
        if guess in rletters:
            n = rletters.index(guess)
            board[n] = guess
            rletters[n] = '$'
            print((' '.join(board)))
            e = wrong + 1
            print('\n'.join(stages[0:e]))
        else:
            wrong += 1
            print((' '.join(board)))
            e = wrong + 1
            print('\n'.join(stages[0:e]))
        if '__' not in board:
            print('You win!')
            print(' '.join(board))
            win = True
            break
    if not win:
        print('\n'.join(stages[0:wrong]))
        print('You lose! It was {}.'.formal(word))

wordlist = ['penis','breast','lunch','apple','acorn','elven','phenomenal','extravagant','piss','brick','phoenix','calzone','zinger','beach','cock','whale','black']
hangman(wordlist[random.randint(0,len(wordlist))])
