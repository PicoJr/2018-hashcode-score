#! /usr/bin/python3

import argparse
import logging

def distance_to_start(position, ride):
    return abs(position[0] - ride[0]) + abs(position[1] - ride[1])


def ride_distance(ride):
    (x1, y1, x2, y2) = ride[0:4]
    return abs(x2 - x1) + abs(y2 - y1)

def check_vehicles(expected, value):
    logging.info("checking vehicles")
    if value != expected:
        logging.warning("some cars are missing from output file")

def check_ride_ids(vehicles_rides):
    rids_assigned = set()
    logging.info("checking ride ids")
    for rids in vehicles_rides:
        for rid in rids:
            if rid in rids_assigned:
                logging.warning("rid {} was assigned more than once".format(rid))
            else:
                rids_assigned.add(rid)

def parse_input(file_in):
    """
    Parse input file
    :param file_in: input file name
    :return: rides_list, rows, columns, vehicles, rides, bonus, steps
    """
    logging.info("parsing rides")
    with open(file_in, 'r') as f:
        logging.info("opening {}".format(file_in))
        first_line = f.readline()
        rows, columns, vehicles, rides, bonus, steps = tuple(map(int, first_line.split(' ')))
        logging.info("{} {} {} {} {} {}".format(rows, columns, vehicles, rides, bonus, steps))
        rides_list = []
        for line in f.readlines():
            logging.debug(line.strip())
            ride = tuple(map(int, line.split(' ')))  # x1, y1, x2, y2, step_start, step_end
            rides_list.append(ride)
    logging.info("done parsing rides")
    return rides_list, rows, columns, vehicles, rides, bonus, steps


def parse_output(file_out):
    """
    Return ride list parsed from output file
    :param file_out: output file name (solution)
    :return: vehicle rides, vr[i] == ride list of vehicle i
    """
    logging.info("parsing {}".format(file_out))
    vehicles_rides = []
    with open(file_out, 'r') as f:
        for line in f.readlines():
            rides = list(map(int, line.split(' ')))
            vehicles_rides.append(rides[1:])  # rides[0] == number of rides
    return vehicles_rides

def eval_ride(ride, step, position, bonus, steps):
    raw_score, bonus_score = 0, 0
    step_min, step_max = ride[4], ride[5]
    step_departure = max(step + distance_to_start(position, ride), step_min)
    new_step = step_departure + ride_distance(ride)  # arrival
    new_position = (ride[2], ride[3])
    if  new_step <= step_max and new_step <= steps:
        raw_score = ride_distance(ride)
        if step + distance_to_start(position, ride) <= step_min:  # bonus
            bonus_score = bonus
    return (raw_score, bonus_score, new_step, new_position)


def compute_score(file_in, file_out, check=False):
    """
    Compute score (with bonus) of submission
    :param file_in: input file
    :param file_out: output file (solution)
    :param check: if True checks cars number and ride ids uniqueness (slower)
    :return: raw_score, bonus_score where total_score = raw_score + bonus_score
    """
    (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(file_in)
    vehicles_rides = parse_output(file_out)
    if check:
        check_vehicles(vehicles, len(vehicles_rides))
        check_ride_ids(vehicles_rides)
    raw_score, bonus_score = 0, 0
    for vehicle, vehicle_rides in enumerate(vehicles_rides):
        position = (0, 0)
        step = 0
        for rid in vehicle_rides:
            ride = rides_list[rid]
            (ride_raw_score, ride_bonus_score, new_step, new_position) = eval_ride(ride, step, position, bonus, steps)
            if ride_raw_score == 0:
                logging.warning("ride {} arrived late".format(rid))
            raw_score += ride_raw_score
            bonus_score += ride_bonus_score
            step = new_step
            position = new_position
    return raw_score, bonus_score

def display_score(raw_score, bonus_score, args):
    if args.score:
        print("score: {0:,} = {1:,} + {2:,} (bonus)".format(raw_score + bonus_score, raw_score, bonus_score))  # decimal separator
    else:
        print("score: {0:,}".format(raw_score + bonus_score))  # decimal separator


def set_log_level(args):
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)


def main():
    parser = argparse.ArgumentParser(description='print score')
    parser.add_argument('file_in', type=str, help='file_in')
    parser.add_argument('file_out', type=str, help='file_out')
    parser.add_argument('--debug', action='store_true', help='for debug purpose')
    parser.add_argument('--score', action='store_true', help='display raw score and bonus score')
    parser.add_argument('--check', action='store_true', help='check output (slower)')
    args = parser.parse_args()
    set_log_level(args)
    (raw_score, bonus_score) = compute_score(args.file_in, args.file_out, args.check)
    display_score(raw_score, bonus_score, args)


if __name__ == '__main__':
    main()
