import random
from word_for_hangman import word_list


def start():
    word = genword()
    underscore(word)
    play(word)


def genword():
    word = random.choice(word_list)
    letters = list(word)
    return word


def underscore(letters):
    num_under = len(letters)
    for i in range(num_under):
        print('_ ', end='')


def play(word):
    letters = list(word)
    while True:
        try:
            print(word)
            for current_index in range(len(letters)):
                guess = input('\nGuess the letter: ')
                for i in range(len(letters)):
                    if guess == letters[current_index]:
                        print('correct')
                        break
                    elif guess == word[i]:
                        
                    else:
                        print('wrong')
                        current_index = current_index - 1
        except ValueError:
            print('put in a letter')


if __name__ == '__main__':
    start()
