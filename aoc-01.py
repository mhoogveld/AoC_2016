#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_01:
    North = 0
    East = 1
    South = 2
    West = 3

    directions = 'L4, L1, R4, R1, R1, L3, R5, L5, L2, L3, R2, R1, L4, R5, R4, L2, R1, R3, L5, R1, L3, L2, R5, L4, L5, R1, R2, L1, R5, L3, R2, R2, L1, R5, R2, L1, L1, R2, L1, R1, L2, L2, R4, R3, R2, L3, L188, L3, R2, R54, R1, R1, L2, L4, L3, L2, R3, L1, L1, R3, R5, L1, R5, L1, L1, R2, R4, R4, L5, L4, L1, R2, R4, R5, L2, L3, R5, L5, R1, R5, L2, R4, L2, L1, R4, R3, R4, L4, R3, L4, R78, R2, L3, R188, R2, R3, L2, R2, R3, R1, R5, R1, L1, L1, R4, R2, R1, R5, L1, R4, L4, R2, R5, L2, L5, R4, L3, L2, R1, R1, L5, L4, R1, L5, L1, L5, L1, L4, L3, L5, R4, R5, R2, L5, R5, R5, R4, R2, L1, L2, R3, R5, R5, R5, L2, L1, R4, R3, R1, L4, L2, L3, R2, L3, L5, L2, L2, L1, L2, R5, L2, L2, L3, L1, R1, L4, R2, L4, R3, R5, R3, R4, R1, R5, L3, L5, L5, L3, L2, L1, R3, L4, R3, R2, L1, R3, R1, L2, R4, L3, L3, L3, L1, L2'

    def __init__(self):
        self.coord_x = 0
        self.coord_y = 0
        self.direction = self.North

    def run(self):
        for instruction in self.directions.split(','):
            self.perform_instruction(instruction.strip())
        return 'Distance: {}'.format(self.coord_x + self.coord_y)

    def perform_instruction(self, instruction):
        instr = re.match('([LR])([1-9][0-9]*)', instruction)
        if instr:
            self.turn(instr.group(1))
            self.walk(instr.group(2))
        else:
            print("Warning: instruction {} not understood".format(instruction))

    def turn(self, dir_instr):
        if dir_instr == 'L':
            self.direction -= 1
        if dir_instr == 'R':
            self.direction += 1
        self.direction %= 4

    def walk(self, dir_steps):
        if self.direction == self.North:
            self.coord_y += int(dir_steps)
        if self.direction == self.East:
            self.coord_x += int(dir_steps)
        if self.direction == self.South:
            self.coord_y -= int(dir_steps)
        if self.direction == self.West:
            self.coord_y -= int(dir_steps)


if __name__ == "__main__":
    solver = AoC_01()
    result = solver.run()
    print(result)
    exit(0)

