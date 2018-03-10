#! /usr/bin/python3

import unittest
from score import compute_score, eval_ride


class TestScore(unittest.TestCase):

    def test_score_a_example(self):
        (raw_score, bonus_score) = compute_score("res/a_example.in", "res/a_example.out")
        self.assertEqual(raw_score, 8)
        self.assertEqual(bonus_score, 2)

    def test_score_b_should_be_easy(self):
        (raw_score, bonus_score) = compute_score("res/b_should_be_easy.in", "res/b_should_be_easy.out")
        self.assertEqual(raw_score, 169677)
        self.assertEqual(bonus_score, 7200)

    def test_possible_ride_with_bonus(self):
        ride = (0, 10, 0, 20, 12, 24)
        bonus = 42
        steps = 26
        step = 0
        position = (0, 0)
        (ride_raw_score, ride_bonus_score, new_step, new_position) = eval_ride(ride, step, position, bonus, steps)
        self.assertEqual(ride_raw_score, 10)
        self.assertEqual(ride_bonus_score, 42)
        self.assertEqual(new_step, 22)
        self.assertEqual(new_position, (0,20))

    def test_possible_ride_without_bonus(self):
        ride = (0, 10, 0, 20, 8, 24)
        bonus = 42
        steps = 26
        step = 0
        position = (0, 0)
        (ride_raw_score, ride_bonus_score, new_step, new_position) = eval_ride(ride, step, position, bonus, steps)
        self.assertEqual(ride_raw_score, 10)
        self.assertEqual(ride_bonus_score, 0)
        self.assertEqual(new_step, 20)
        self.assertEqual(new_position, (0,20))

    def test_impossible_ride(self):
        ride = (0, 10, 0, 20, 6, 18)
        bonus = 42
        steps = 26
        step = 0
        position = (0, 0)
        (ride_raw_score, ride_bonus_score, new_step, new_position) = eval_ride(ride, step, position, bonus, steps)
        self.assertEqual(ride_raw_score, 0)
        self.assertEqual(ride_bonus_score, 0)
        self.assertEqual(new_step, 20)
        self.assertEqual(new_position, (0,20))

    def test_impossible_ride_simulation_step(self):
        ride = (0, 4, 0, 20, 2, 22)
        bonus = 42
        steps = 10
        step = 0
        position = (0, 0)
        (ride_raw_score, ride_bonus_score, new_step, new_position) = eval_ride(ride, step, position, bonus, steps)
        self.assertEqual(ride_raw_score, 0)
        self.assertEqual(ride_bonus_score, 0)
        self.assertEqual(new_step, 20)
        self.assertEqual(new_position, (0,20))

if __name__ == '__main__':
    unittest.main()
