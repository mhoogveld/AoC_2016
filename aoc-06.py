#!/usr/bin/python

import hashlib
from sys import hash_info
import operator

__author__ = "m.hoogveld@elevate.nl"

class AoC_06:
    def __init__(self):
        pass

    def run(self):
        signal_most = dict()
        signal_least = dict()
        pos_dict = dict()
        input_file = 'input-06'

        # count chars at positions
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                line = line.strip()
                pos = 0
                for char in line:
                    # init position in dictionary
                    if pos not in pos_dict:
                        pos_dict[pos] = dict()

                    # init char at this position
                    if char not in pos_dict[pos]:
                        pos_dict[pos][char] = 0

                    # add count for this char at this position
                    pos_dict[pos][char] += 1

                    pos += 1

        for pos, value in pos_dict.items():
            sorted_pos = self.sort_dict_by_value(pos_dict[pos])
            most_common_char, count = sorted_pos[-1]
            least_common_char, count = sorted_pos[0]
            signal_most[pos] = most_common_char
            signal_least[pos] = least_common_char

        msg_most = ''.join(signal_most.values())
        msg_least = ''.join(signal_least.values())
        print("Message by most common characters is {}".format(msg_most))
        print("Message by least common characters is {}".format(msg_least))

    @staticmethod
    def sort_dict_by_value(dict_in):
        return sorted(dict_in.items(), key=operator.itemgetter(1))

if __name__ == "__main__":
    solver = AoC_06()
    solver.run()
    exit(0)

