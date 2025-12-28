word = "world"

line = ["_"] * len(word)
attempts = 6
guessed = set()

print('Welcome to Hangman!')
print(' '.join(line))

while attempts > 0 and '_' in line:
    guess = input('Guess a letter: ').strip().lower()
    if not guess or len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue
    if guess in guessed:
        print('You already guessed:', guess)
        continue
    guessed.add(guess)

    if guess in word:
        for idx, ch in enumerate(word):
            if ch == guess:
                line[idx] = guess
        print('Correct:', ' '.join(line))
    else:
        attempts -= 1
        print(f'Wrong. Attempts left: {attempts}')
        print(' '.join(line))

if '_' not in line:
    print('You win! The word was', word)
else:
    print('You lost. The word was', word)


