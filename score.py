#! /usr/bin/python3

import argparse
import logging

def distance_to_start(position, ride):
    return abs(position[0] - ride[0]) + abs(position[1] - ride[1])


def ride_distance(ride):
    (x1, y1, x2, y2) = ride[0:4]
    return abs(x2 - x1) + abs(y2 - y1)


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


def compute_score(file_in, file_out):
    """
    Compute score (with bonus) of submission
    :param file_in: input file
    :param file_out: output file (solution)
    :return: raw_score, bonus_score where total_score = raw_score + bonus_score
    """
    (rides_list, rows, columns, vehicles, rides, bonus, steps) = parse_input(file_in)
    vehicles_rides = parse_output(file_out)
    raw_score = 0
    bonus_score = 0
    for vehicle, vehicle_rides in enumerate(vehicles_rides):
        position = (0, 0)
        step = 0
        for rid in vehicle_rides:
            ride = rides_list[rid]
            step_min = ride[4]
            step_max = ride[5]
            if step + distance_to_start(position, ride) + ride_distance(ride) <= step_max:
                raw_score += ride_distance(ride)
                if step + distance_to_start(position, ride) <= step_min:  # bonus
                    bonus_score += bonus
                step_departure = max(step + distance_to_start(position, ride), step_min)
                step = step_departure + ride_distance(ride)
                position = (ride[2], ride[3])
            else:
                logging.error("invalid ride")
    return raw_score, bonus_score


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
    args = parser.parse_args()
    set_log_level(args)
    (raw_score, bonus_score) = compute_score(args.file_in, args.file_out)
    if args.score:
        print("score: {0:,} = {1:,} + {2:,} (bonus)".format(raw_score + bonus_score, raw_score, bonus_score))  # decimal separator
    else:
        print("score: {0:,}".format(raw_score + bonus_score))  # decimal separator


if __name__ == '__main__':
    main()
