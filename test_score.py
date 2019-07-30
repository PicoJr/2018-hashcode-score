#! /usr/bin/python3

import logging
import unittest

from score import Car, Ride, Score
from score import check_vehicles, check_ride_ids
from score import compute_score, eval_ride
from score import parse_input, parse_output

RES_FOLDER = 'res/'
logging.basicConfig(level=logging.ERROR)  # disables warnings


class TestScore(unittest.TestCase):
    def test_score_a_example(self):
        score = compute_score(RES_FOLDER + "a_example.in", RES_FOLDER + "a_example.out")
        self.assertEqual(score.raw_score, 8)
        self.assertEqual(score.bonus_score, 2)

    def test_score_b_should_be_easy(self):
        score = compute_score(RES_FOLDER + "b_should_be_easy.in",
                              RES_FOLDER + "b_should_be_easy.out")
        self.assertEqual(score.raw_score, 169677)
        self.assertEqual(score.bonus_score, 7200)

    def test_possible_ride_with_bonus(self):
        car = Car()
        car.step = 0
        car.x, car.y = 0, 0
        ride = Ride(0, 0, 10, 0, 20, 12, 24)
        bonus = 42
        steps = 26
        score = Score()
        eval_ride(car, ride, score, bonus, steps)
        self.assertEqual(score.raw_score, 10)
        self.assertEqual(score.bonus_score, 42)
        self.assertEqual(car.step, 22)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 20)

    def test_possible_ride_without_bonus(self):
        car = Car()
        car.step = 0
        car.x, car.y = 0, 0
        ride = Ride(0, 0, 10, 0, 20, 8, 24)
        bonus = 42
        steps = 26
        score = Score()
        eval_ride(car, ride, score, bonus, steps)
        self.assertEqual(score.raw_score, 10)
        self.assertEqual(score.bonus_score, 0)
        self.assertEqual(car.step, 20)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 20)

    def test_impossible_ride(self):
        car = Car()
        car.step = 0
        car.x, car.y = 0, 0
        ride = Ride(0, 0, 10, 0, 20, 6, 18)
        bonus = 42
        steps = 26
        score = Score()
        eval_ride(car, ride, score, bonus, steps)
        self.assertEqual(score.raw_score, 0)
        self.assertEqual(score.bonus_score, 0)
        self.assertEqual(car.step, 20)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 20)

    def test_impossible_ride_simulation_step(self):
        car = Car()
        car.step = 0
        car.x, car.y = 0, 0
        ride = Ride(0, 0, 4, 0, 20, 2, 22)
        bonus = 42
        steps = 10
        score = Score()
        eval_ride(car, ride, score, bonus, steps)
        self.assertEqual(score.raw_score, 0)
        self.assertEqual(score.bonus_score, 0)
        self.assertEqual(car.step, 20)
        self.assertEqual(car.x, 0)
        self.assertEqual(car.y, 20)

    def test_valid_vehicles_a(self):
        (_rides_list, _rows, _columns, vehicles, _rides, _bonus, _steps) = parse_input(RES_FOLDER + "a_example.in")
        vehicles_rides = parse_output(RES_FOLDER + "a_example.out")
        self.assertTrue(check_vehicles(vehicles, len(vehicles_rides)))

    def test_valid_vehicles_b(self):
        (_rides_list, _rows, _columns, vehicles, _rides, _bonus, _steps) = parse_input(
            RES_FOLDER + "b_should_be_easy.in")
        vehicles_rides = parse_output(RES_FOLDER + "b_should_be_easy.out")
        self.assertTrue(check_vehicles(vehicles, len(vehicles_rides)))

    def test_valid_rids_a(self):
        (_rides_list, _rows, _columns, _vehicles, rides, _bonus, _steps) = parse_input(RES_FOLDER + "a_example.in")
        vehicles_rides = parse_output(RES_FOLDER + "a_example.out")
        self.assertTrue(check_ride_ids(vehicles_rides, rides))

    def test_valid_rids_b(self):
        (_rides_list, _rows, _columns, _vehicles, rides, _bonus, _steps) = parse_input(
            RES_FOLDER + "b_should_be_easy.in")
        vehicles_rides = parse_output(RES_FOLDER + "b_should_be_easy.out")
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
