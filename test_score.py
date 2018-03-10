#! /usr/bin/python3

import logging
import unittest

from score import check_vehicles, check_ride_ids
from score import compute_score, eval_ride
from score import parse_input, parse_output

res_folder = 'res/'
logging.basicConfig(level=logging.ERROR)  # disables warnings


class TestScore(unittest.TestCase):
    def test_score_a_example(self):
        (raw_score, bonus_score) = compute_score(res_folder + "a_example.in", res_folder + "a_example.out")
        self.assertEqual(raw_score, 8)
        self.assertEqual(bonus_score, 2)

    def test_score_b_should_be_easy(self):
        (raw_score, bonus_score) = compute_score(res_folder + "b_should_be_easy.in",
                                                 res_folder + "b_should_be_easy.out")
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
        self.assertEqual(new_position, (0, 20))

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
        self.assertEqual(new_position, (0, 20))

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
        self.assertEqual(new_position, (0, 20))

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
        self.assertEqual(new_position, (0, 20))

    def test_valid_vehicles_a(self):
        (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(res_folder + "a_example.in")
        vehicles_rides = parse_output(res_folder + "a_example.out")
        self.assertTrue(check_vehicles(vehicles, len(vehicles_rides)))

    def test_valid_vehicles_b(self):
        (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(res_folder + "b_should_be_easy.in")
        vehicles_rides = parse_output(res_folder + "b_should_be_easy.out")
        self.assertTrue(check_vehicles(vehicles, len(vehicles_rides)))

    def test_valid_rids_a(self):
        (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(res_folder + "a_example.in")
        vehicles_rides = parse_output(res_folder + "a_example.out")
        self.assertTrue(check_ride_ids(vehicles_rides, rides))

    def test_valid_rids_b(self):
        (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(res_folder + "b_should_be_easy.in")
        vehicles_rides = parse_output(res_folder + "b_should_be_easy.out")
        self.assertTrue(check_ride_ids(vehicles_rides, rides))

    def test_invalid_rids_range(self):
        rides = 10
        vehicles_rides = [[1, 2, 3], [12]]
        self.assertFalse(check_ride_ids(vehicles_rides, rides))

    def test_invalid_rids_assigned_more_than_once(self):
        rides = 10
        vehicles_rides = [[1, 2, 3], [2, 8]]
        self.assertFalse(check_ride_ids(vehicles_rides, rides))

if __name__ == '__main__':
    unittest.main()
