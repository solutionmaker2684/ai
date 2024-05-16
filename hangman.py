import random

def choose_word():
    words = ['python', 'hangman', 'computer', 'keyboard', 'mouse', 'monitor', 'program', 'algorithm']
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ''
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += '_'
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    while True:
        print("\nWord:", display_word(word, guessed_letters))
        print("Attempts left:", attempts)
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print("Incorrect guess!")

            if attempts == 0:
                print("You lost! The word was:", word)
                break
        else:
            print("Correct guess!")

        if all(letter in guessed_letters for letter in word):
            print("Congratulations! You won!")
            break

        if attempts == 0:
            print("You lost! The word was:", word)
            break

hangman()
