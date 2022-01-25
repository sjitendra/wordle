# Wordle

Guess the word in 6 tries.

This is the game of guessing 5 letter words in 6 tries.

After each try/guess, guess word will be shown with the colors to show how close your guess was to the word.


## Installing dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```shell
pip install -r requirements.txt
```

## How to play

```python

# run the program (on Python 3.x) - wordle.py
$ python wordle.py
----------- WORDLE -----------
# enter the guess e.g. here 'GREAT'
Guess 1 - please enter the word: GREAT
GREAT

# 2nd guess
Guess 2 - please enter the word: TODAY
TODAY

# 3rd guess
Guess 3 - please enter the word: OBEYS
OBEYS

# 4th guess
Guess 4 - please enter the word: PACER
PACER

# 5th guess
Guess 5 - please enter the word: LOOKS
LOOKS

# 6th guess
Guess 6 - please enter the word: PROXY
PROXY

# result of the game..
Phew! You won.
```

#### Significance of the colors given to the letters of a guessed word
    GREEN  - When letter is in the correct spot of the word
    YELLOW - When letter is in the word but not in the correct spot
    WHITE  - When Letter is not in the word.


## License
[Apache 2.0](https://choosealicense.com/licenses/apache-2.0/)
