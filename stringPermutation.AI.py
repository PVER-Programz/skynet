def find_correct_characters(guess, target):
    correct_characters = [g if g == t else '_' for g, t in zip(guess, target)]
    return ''.join(correct_characters)

def update_possible_characters(previous_guesses, target):
    possible_characters = []

    for i in range(len(target)):
        char_set = set()
        for guess in previous_guesses:
            char_set.add(guess[i])
        possible_characters.append(char_set)

    return possible_characters

def guess_string(target_string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    string_length = len(target_string)
    alphabet_length = len(alphabet)

    guess_number = 1  # Initialize guess number
    previous_guesses = []

    # Initialize possible characters for each position
    possible_characters = [set(alphabet) for _ in range(string_length)]

    while True:
        # Create a guess based on the possible characters for each position
        guess = ''.join([next(iter(char_set)) for char_set in possible_characters])

        correct_characters = find_correct_characters(guess, target_string)
        correct_chars_count = sum(g == t for g, t in zip(guess, target_string))
        
        print(f"Guess {guess_number}: {guess}, Correct Characters: {correct_characters}, Correct Characters Count: {correct_chars_count}")

        if correct_characters == target_string:
            print(f"Guessed string: {guess}")
            break

        # Update possible characters based on the correct characters in the guess
        for i, char in enumerate(guess):
            if char != target_string[i]:
                possible_characters[i].discard(char)

        # Add the guess to the list of previous guesses
        previous_guesses.append(guess)

        guess_number += 1  # Increment guess number

# Get input from the user
input_string = input("Enter a string to guess: ").lower()

# Guess the string
guess_string(input_string)
