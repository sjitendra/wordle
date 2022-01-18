from unittest.mock import patch
import unittest

import wordle


class WordleGameTest(unittest.TestCase):


    @patch('wordle.input', return_value='PROXY')
    def test_winning_streak(self, input):
        w = wordle.Wordle("PROXY")
        w.play()
        self.assertTrue(w.result)

    @patch('wordle.input', return_value='PROXY')
    def test_losing_streak(self, input):
        w = wordle.Wordle("GREEN")
        w.play()
        self.assertFalse(w.result)


class WordValidityTest(unittest.TestCase):

    def test_valid_word(self):
        self.assertTrue(wordle.is_word_valid("TODAY"))
        self.assertTrue(wordle.is_word_valid("GREAT"))
        self.assertTrue(wordle.is_word_valid("important"))

    def test_invalid_word(self):
        self.assertFalse(wordle.is_word_valid("TODYA"))
        self.assertFalse(wordle.is_word_valid("DDMM"))