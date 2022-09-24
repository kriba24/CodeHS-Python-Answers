count = 0
secret_word = "amogus"
def get_guess(word):
    while True:
        if not word.islower():
            print('Your guess must be a lowercase letter!')
            break
        elif len(word) > 1:
            print('Your guess must be a lowercase letter!')
            break
        else:
            return word
while count < 10:
    guess = input('Guess: ')
    get_guess(guess)
    if guess in secret_word:
        print('That letter is in the secret word!')
    elif guess not in secret_word:
        print('That letter is not in the secret word!')
    count += 1