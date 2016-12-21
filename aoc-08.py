#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_08:
    def __init__(self):
        self.screen_width = 50
        self.screen_height = 6
        # Initialize screen of dimensions width by height with pixels turned off (0)
        self.screen = [['.' for x in range(self.screen_width)] for y in range(self.screen_height)]

    def run(self):
        input_file = 'input-08'
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                instruction = line.strip()
                print(instruction)
                self.perform(instruction)
                self.print_screen()
        self.print_pixel_count()

    def perform(self, instruction):
        rect_re = r"rect (\d+)x(\d+)"
        rotate_row_re = r"rotate row y=(\d+) by (\d+)"
        rotate_col_re = r"rotate column x=(\d+) by (\d+)"

        rect_match = re.match(rect_re, instruction)
        if rect_match:
            width = int(rect_match.group(1))
            height = int(rect_match.group(2))
            self.rect(width, height)
            return

        rotate_row_match = re.match(rotate_row_re, instruction)
        if rotate_row_match:
            row = int(rotate_row_match.group(1))
            amount = int(rotate_row_match.group(2))
            self.rotate_row(row, amount)
            return

        rotate_col_match = re.match(rotate_col_re, instruction)
        if rotate_col_match:
            col = int(rotate_col_match.group(1))
            amount = int(rotate_col_match.group(2))
            self.rotate_col(col, amount)
            return

    def print_screen(self):
        for row in self.screen:
            print("".join(row))
        print()

    def print_pixel_count(self):
        on = 0
        off = 0
        for row in self.screen:
            on += row.count("#")
            off += row.count(".")
        print("Pixels on: {}, pixels off: {}".format(on, off))

    def rect(self, width, height):
        if width < 0 or width >= self.screen_width:
            raise RuntimeError
        if height < 0 or height >= self.screen_height:
            raise RuntimeError

        for row_nr in range(0, height):
            for col_nr in range(0, width):
                self.screen[row_nr][col_nr] = '#'

    def rotate_row(self, row_nr, amount):
        if row_nr < 0 or row_nr >= self.screen_height:
            raise RuntimeError

        self.screen[row_nr] = AoC_08.rotate_arr(self.screen[row_nr], amount)

    def rotate_col(self, col_nr, amount):
        if col_nr < 0 or col_nr >= self.screen_width:
            raise RuntimeError

        col_values = []
        for row in self.screen:
            col_values.append(row[col_nr])

        col_values = AoC_08.rotate_arr(col_values, amount)

        for row_nr in range(0, self.screen_height):
            self.screen[row_nr][col_nr] = col_values[row_nr]

    @staticmethod
    def rotate_arr(arr, amount):
        return arr[-amount:] + arr[:-amount]


if __name__ == "__main__":
    solver = AoC_08()
    solver.run()
    exit(0)

