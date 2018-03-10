#! /usr/bin/python3

import unittest
from score import compute_score


class TestScore(unittest.TestCase):

    def test_score_a_example(self):
        (raw_score, bonus_score) = compute_score("res/a_example.in", "res/a_example.out")
        self.assertEqual(raw_score, 8)
        self.assertEqual(bonus_score, 2)

    def test_score_b_should_be_easy(self):
        (raw_score, bonus_score) = compute_score("res/b_should_be_easy.in", "res/b_should_be_easy.out")
        self.assertEqual(raw_score, 169677)
        self.assertEqual(bonus_score, 7200)


if __name__ == '__main__':
    unittest.main()
