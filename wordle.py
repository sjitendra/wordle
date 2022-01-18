"""
This module is for Wordle game.
"""
import random

from colorama import Fore, Style
from spellchecker import SpellChecker


# 5 letter english word corpus
WORD_CORPUS = [
    'TODAY',
    'LUCKY',
    'GREAT',
    'PROXY',
    'GREEN',
    'AUDIO',
    'ABOVE',
    'THINK',
    'LEARN',
    'HOURS'
]
MAX_TRIALS = 6
WORD_LENGTH = 5
spell_checker = SpellChecker()  # To check the word.


def is_word_valid(word):
    return spell_checker.correction(word) == word


def validate_word(word):
    """Validates the user guesses.
    """
    error_msg = None
    if len(word) != WORD_LENGTH:
        error_msg = f"Word should be of {WORD_LENGTH} letters"
    elif not is_word_valid(word):
        error_msg = "Not a valid word..! Please try with a valid english word"

    return not bool(error_msg), error_msg


class Wordle:

    def __init__(self, daily_word=None):
        if daily_word:
            self.daily_word = daily_word.upper()
        else:
            self.daily_word = random.choice(WORD_CORPUS)
        self.result = None

    def check(self, word):
        output = list()
        correct_spot_count = 0

        for i, char in enumerate(word):
            color = Fore.WHITE
            if char == self.daily_word[i]:
                color = Fore.GREEN
                correct_spot_count += 1
            elif char in self.daily_word:
                color = Fore.YELLOW

            output.append((color, char))

        self.result = correct_spot_count == len(word)
        return output

    def print_guessed_word(self, output):
        """Prints the guessed word to the terminal
        """
        output_str = ""
        for color, char in output:
            output_str += color + char

        print(output_str)
        print(Style.RESET_ALL)

    def play(self):

        print("----------- WORDLE -----------")
        trial = 1

        while trial <= MAX_TRIALS:
            word = input(f"Guess {trial} - please enter the word: ")

            is_valid, error_msg = validate_word(word)
            if not is_valid:
                print("Error - ", error_msg)
                continue

            word = word.upper()
            output = self.check(word)
            self.print_guessed_word(output)

            if self.result:
                print("Phew! You won.")
                break

            trial += 1

        if not self.result:
            print("You lost..Better luck next time!")


if __name__ == '__main__':
    w = Wordle()
    w.play()

"""
Assumptions
- For this program, considered 5 letter word corpus of 10 word as of now.
- For each code run, one word is chosen randomly from the word corpus.
- Significance of the colors given to the letters of a guessed word
    - Green - Letter is in right spot of the word
    - YELLOW - Letter is in the word but not in right spot
    - WHITE - Letter is not in the word.

Input Validations
- don't allow spaces..it should be of 5 chars.. use isalpha and len
- check if the word is a valid english word

Make below Checks for each letters if word is valid english work
- if it's at right spot
- if it's present in the word
- Otherwise its not valid choice..

Print the output with a colored letters in caps form

Test cases
    - Guessing the Correct word
    - Guessing Somehow close word 
    - Invalid word..
"""