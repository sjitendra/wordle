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

    Args;
        word: Guess word entered by an User.

    Returns:
        is_valid flag and error message if any.
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
        """Checks the guess with the daily word and
        assigns colors to the letters of the entered word.
        Also concludes the result.

        Args:
            word: User entered guess input.
        """
        output = list()
        correct_spot_count = 0
        color_choices = dict()  # To maintain color choice of each letter
        daily_word_letter_freq = dict()

        # Calculating Letter frequencies in the daily word
        for char in self.daily_word:
            daily_word_letter_freq[char] = daily_word_letter_freq.get(char, 0) + 1

        for i, char in enumerate(word):
            if char == self.daily_word[i]:
                correct_spot_count += 1
                color_choices[i] = Fore.GREEN
                daily_word_letter_freq[char] -= 1
            elif char not in self.daily_word:
                color_choices[i] = Fore.WHITE

        for i, char in enumerate(word):
            if i not in color_choices:
                if daily_word_letter_freq[char]:
                    color_choices[i] = Fore.YELLOW
                    daily_word_letter_freq[char] -= 1
                else:
                    color_choices[i] = Fore.WHITE

        for i, char in enumerate(word):
            output.append((color_choices[i], char))

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
- For this program, considered 5 letter word corpus of 10 words as of now.
- For each code run, one word is chosen randomly from the word corpus.
- Significance of the colors given to the letters of a guessed word
    - GREEN - Letter is in right spot of the word
    - YELLOW - Letter is in the word but not in right spot
    - WHITE - Letter is not in the word.

Input Validations
- not allowing spaces
- word should be of 5 chars
- check if the word is a valid english word

Make below checks for each letters if the guess is valid english word
- if it's at right spot
- if it's present in the word
- Otherwise its not valid choice.
and then print the output with a colored letters in caps form

Test cases
    - Guessing the Correct word
    - Guessing the somehow close word
    - Invalid and valid word checks
"""
