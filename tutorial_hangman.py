import random
from word_for_hangman import word_list
tries = 50
letter_guess = ''
def start():
    print('Hangman: \n')
    #word = random.choice(word_list)
    word = 'secret'
    under(word, tries)


def under(word, tries):
    while tries > 0:
        try:
            for char in word:
                if char in letter_guess:
                    print(letter_guess, end='')
                else:
                    print('_', end='')
            if letter_guess not in word:
                tries -= 1
                print()
                print(f'wrong you have {tries} tries left')
            ask()
        except ValueError:
            print('skibdi toilet ohio fanum tax rizzler gyatt')
        if tries == 0:
            print('lost')

def ask():
    while True:
        try:
            global letter_guess
            letter_guess = input('\nchoose a letter: ')
            if len(list(letter_guess)) == 1:
                return letter_guess
            else:
                print('put in 1 letter')
        except ValueError:
            print('put in a single letter')


if __name__ == '__main__':
    start()
