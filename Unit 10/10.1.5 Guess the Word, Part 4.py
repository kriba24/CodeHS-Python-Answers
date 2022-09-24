import random
words = ['amogus', 'impostor', 'sus', 'baka']
secret_word = random.choice(words)
dashes = '-' * len(secret_word)
def get_guess():
    while True:
        guess = input('Guess: ')
        if not guess.islower():
            print('Your guess must be a lowercase letter!')
            break
        elif len(guess) > 1:
            print('Your guess must be a lowercase letter!')
            break
        else:
            return guess
def update_dashes(secret_word, dashes, guess):
    result = ""
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            result += guess
        else:
            result += dashes[i]
    return result
guesses_left = 10
while guesses_left > 0 or dashes != secret_word:
    print(dashes)
    print(str(guesses_left) + ' incorrect guesses left.')
    guessword = input('Would you like to guess the word(y/n)? ')
    # if not guessword:
    #     print('Try again!')
    if guessword.lower() == "y":
        guess = input('Guess: ')
        if guess.lower() == secret_word:
            print('You win!')
            break
        elif guess != secret_word:
            print('That\'s not the word!')
            guesses_left -= 2
    elif guessword.lower() == "n":
        guess = get_guess()
        dashes = update_dashes(secret_word, dashes, guess)
        if guess in secret_word:
            print('That letter is in the secret word!')
        elif guess not in secret_word:
            print('That letter is not in the secret word!')
            guesses_left -= 1
        if dashes == secret_word:
            print('You win!')
            break
        elif guesses_left == 0:
            print('You lose!')
            break

print('The secret word was: ' + secret_word)