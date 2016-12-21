#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_09:
    def __init__(self):
        pass

    def run(self):
        input_file = 'input-09'
        decompressed_data = ""
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                data = line.strip()
                decompressed_data += self.decompress(data)
        print("Length of decompressed data = {}".format(len(decompressed_data)))

    def test(self, input):
        print("Data = {}\nDecompressed = {}".format(input, self.decompress(input)))

    def decompress(self, data):
        instr_re = r"(.*)\((\d+)x(\d+)\)(.*)"

        m = re.search(instr_re, data)
        if not m:
            return data
        else:
            before = m.group(1)
            rep_len = int(m.group(2))
            rep_count = int(m.group(3))
            after = m.group(4)

            decompressed_data = before + (after[:rep_len] * rep_count)
            return decompressed_data + self.decompress(after[rep_len:])


if __name__ == "__main__":
    solver = AoC_09()
    solver.test("ADVENT")
    solver.test("A(1x5)BC")
    solver.test("(3x3)XYZ")
    solver.test("A(2x2)BCD(2x2)EFG  ")
    solver.test("(6x1)(1x3)A")
    solver.test("X(8x2)(3x3)ABCY")
    # solver.run()
    exit(0)

