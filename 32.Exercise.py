def word_game(input_word=None):
    # Get a word from the user or use the provided input
    if input_word is None:
        word = input("Enter a word: ")
    else:
        word = input_word

    # Task 1: Find the length of the word
    word_length = len(word)

    # Task 2: Print the word and its length
    print(f"The word '{word}' has {word_length} characters")

    # Task 3: Reverse the word
    word_reversed = word[::-1]

    # Task 4: Print the reversed word
    print(f"The reversed word is: {word_reversed}")

    # Task 5: Create a new word by repeating the first character
    first_char = word[0] * word_length

    # Task 6: Print the new word
    print(f"A new word created by repeating the first character: {first_char}")

    # Task 7: Concatenate the original word with a suffix
    suffix = "ish"
    word_with_suffix = word + suffix

    # Task 8: Print the word with suffix
    print(f"The word with the suffix 'ish': {word_with_suffix}")

    # Task 9: Convert the word to uppercase
    word_upper = word.upper()

    # Task 10: Print the uppercase word
    print(f"The word in uppercase: {word_upper}")

    # Task 11: Replace a character in the word
    word_replace = word.replace("l","x")

    # Task 12: Print the word with replaced character
    print(f"The word with 'l' replaced by 'x': {word_replace}")

if __name__ == "__main__":
    word_game()

# Hints:
# - Use len() function to find the length of a string
# - Use string slicing with a step of -1 to reverse a string
# - Use the * operator for string repetition
# - Use the + operator for string concatenation
# - Use the upper() method to convert a string to uppercase
# - Use the replace() method to replace characters in a string
# - Use f-strings for formatted output