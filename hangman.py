import random

# Word list
word_list = ['Ronak', 'riya', 'ritik']
word = random.choice(word_list).lower()  # Convert to lowercase for consistency

# Track guessed letters
guessed_letters = []

# Game loop
for _ in range(10):
    letter = input('Guess a letter: ').lower()

    if letter in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.append(letter)

    # Display current progress
    display = ''
    for char in word:
        if char in guessed_letters:
            display += char
        else:
            display += '_'

    print(display)

    # Check for win condition
    if '_' not in display:
        print('You Win!')
        break
else:
    print(f'Sorry, you lost. The word was "{word}".')
