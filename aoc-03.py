#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_03:
    def __init__(self):
        pass

    def run(self):
        triangle_input_file = "input-03"

        h_triangle_count = self.horizontal_triangle_count(triangle_input_file)
        v_triangle_count = self.vertical_triangle_count(triangle_input_file)

        print("Number of possible horizontal triangles: {}".format(h_triangle_count))
        print("Number of possible vertical triangles: {}".format(v_triangle_count))

    def horizontal_triangle_count(self, triangle_input_file):
        triangle_count = 0
        with open(triangle_input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                sides_match = re.match("[^\d]*(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]*", line)
                if sides_match:
                    triangle_def = [sides_match.group(1), sides_match.group(2), sides_match.group(3)]
                    if self.is_triangle(triangle_def):
                        triangle_count += 1
        return triangle_count

    def vertical_triangle_count(self, triangle_input_file):
        triangle_count = 0
        triangle_defs = [[], [], []]
        with open(triangle_input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                sides_match = re.match("[^\d]*(\d+)[^\d]+(\d+)[^\d]+(\d+)[^\d]*", line)
                if sides_match:
                    triangle_defs[0].append(sides_match.group(1))
                    triangle_defs[1].append(sides_match.group(2))
                    triangle_defs[2].append(sides_match.group(3))
                    if len(triangle_defs[0]) == 3:
                        for triangle_def in triangle_defs:
                            if self.is_triangle(triangle_def):
                                triangle_count += 1
                        triangle_defs = [[], [], []]

        return triangle_count

    def is_triangle(self, sides):
        if not len(sides) == 3:
            return False

        try:
            sides = list(map(int, sides))
            sides.sort()
            return sides[0] + sides[1] > sides[2]

        except ValueError:
            return False

if __name__ == "__main__":
    solver = AoC_03()
    solver.run()
    exit(0)

