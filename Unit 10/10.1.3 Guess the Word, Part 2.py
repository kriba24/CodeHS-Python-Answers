secret_word = "amogus"
dashes = '-' * len(secret_word)

def get_guess():
    guess = input('Guess: ')
    if not guess.islower():
        print('Your guess must be a lowercase letter!')
    elif len(guess) > 1:
        print('Your guess must be a lowercase letter!')
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

count = 0
while count < 10:
    guess = get_guess()
    if guess in secret_word:
        print('That letter is in the secret word!')
    elif guess not in secret_word:
        print('That letter is not in the secret word!')
    dashes = update_dashes(secret_word, dashes, guess)
    print(dashes)
    count += 1