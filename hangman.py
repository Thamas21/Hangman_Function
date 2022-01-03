import random
from word_list import words


def pick_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word


def hangman():
    word = pick_word(words)
    word_set = set(word)
    guess_list = []
    guess_list = set(guess_list)
    letter_guessed = []
    for letter in word:
        print('_', end=" ")
    while guess_list != word_set:
        guessed = ', '.join(letter_guessed).upper()
        print(f'\n\nYou have guessed {guessed}')
        guess = input('\n\nGuess a letter! ')
        letter_guessed.append(guess)
        guess = guess.lower()
        if guess in word:
            guess_list.add(guess)
        elif guess != guess.isalpha() or len(guess) > 3:
            print("Try again!")
        for letter in word:
            if letter in guess_list:
                print(f'{letter}', end="")
            else:
                print("_", end=" ")
    print("\nYou win!")
    play_again = input('Do you want to play again? ')
    play_again = play_again.upper()
    if play_again == 'Y' or play_again == "YES":
        hangman()
    else:
        print('Ok bye bye!')


hangman()
#print(len(words))