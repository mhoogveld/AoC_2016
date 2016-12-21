#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_09:
    def __init__(self):
        pass

    def run(self, ver=1):
        input_file = 'input-09'
        decompressed_data = ""
        decompressed_data_len = 0
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                data = line.strip()
                # decompressed_data += self.decompress(data, ver)
                decompressed_data_len += self.decompress_len(data, ver)
        # print("Length of decompressed data (version {}) = {}".format(ver, len(decompressed_data)))
        print("Length of decompressed data (version {}) = {}".format(ver, decompressed_data_len))

    def test(self, input, ver=1):
        dec_data = self.decompress(input, ver)
        print("Data = {}\nDecompressed (len: {}) = {}".format(input, len(dec_data), dec_data))

    def decompress(self, data, ver=1):
        instr_re = r"(.*?)\((\d+)x(\d+)\)(.*)"

        m = re.search(instr_re, data)
        if not m:
            return data
        else:
            before = m.group(1)
            rep_len = int(m.group(2))
            rep_count = int(m.group(3))
            after = m.group(4)

            if ver == 2:
                decompressed_data = before + str(self.decompress(after[:rep_len], ver) * rep_count)
                decompressed_data += self.decompress(after[rep_len:], ver)
            else:
                decompressed_data = before + str(after[:rep_len] * rep_count)
                decompressed_data += self.decompress(after[rep_len:], ver)
            return decompressed_data

    def decompress_len(self, data, ver=1):
        instr_re = r"(.*?)\((\d+)x(\d+)\)(.*)"

        m = re.search(instr_re, data)
        if not m:
            return len(data)
        else:
            length = len(m.group(1))
            rep_len = int(m.group(2))
            rep_count = int(m.group(3))
            after = m.group(4)

            if ver == 2:
                length += self.decompress_len(after[:rep_len], ver) * rep_count
                length += self.decompress_len(after[rep_len:], ver)
            else:
                length += len(after[:rep_len]) * rep_count
                length += self.decompress_len(after[rep_len:], ver)
            return length


if __name__ == "__main__":
    solver = AoC_09()
    solver.test("ADVENT")
    solver.test("A(1x5)BC")
    solver.test("(3x3)XYZ")
    solver.test("A(2x2)BCD(2x2)EFG  ")
    solver.test("(6x1)(1x3)A")
    solver.test("X(8x2)(3x3)ABCY")

    solver.test("(3x3)XYZ", 2)
    solver.test("X(8x2)(3x3)ABCY", 2)
    solver.test("(27x12)(20x12)(13x14)(7x10)(1x12)A", 2)
    solver.test("(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN", 2)

    solver.run()
    solver.run(2)
    exit(0)

