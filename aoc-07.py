#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_07:
    def __init__(self):
        pass

    def run(self):
        tls_support_count = 0
        input_file = 'input-07'

        # count chars at positions
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                line = line.strip()
                if AoC_07.supports_tls(line):
                    tls_support_count += 1

        print("Support count {}".format(tls_support_count))

    @staticmethod
    def test_tls(test):
        print("Test TLS for {}. Result is {}".format(test, AoC_07.supports_tls(test)))

    @staticmethod
    def test_abba(test):
        print("Test ABBA for {}. Result is {}".format(test, AoC_07.contains_abba(test)))

    @staticmethod
    def supports_tls(ipv7_address):
        for part in re.findall(r"\[([a-z]+)\]", ipv7_address):
            if AoC_07.contains_abba(part):
                return False

        for part in re.findall(r"^([a-z]+)\[", ipv7_address):
            if AoC_07.contains_abba(part):
                return True
        for part in re.findall(r"\]([a-z]+)\[", ipv7_address):
            if AoC_07.contains_abba(part):
                return True
        for part in re.findall(r"\]([a-z]+)$", ipv7_address):
            if AoC_07.contains_abba(part):
                return True

        return False

    @staticmethod
    def contains_abba(abba_input):
        abba_input = re.sub(r"([a-z])\1\1\1", r"\1\1", abba_input)
        abba_re = r"([a-z])([^\1])\2\1"
        return re.search(abba_re, abba_input) is not None

if __name__ == "__main__":
    # AoC_07.test_abba("asderreasdp")
    # AoC_07.test_abba("dddd")
    # AoC_07.test_abba("qwewerert")
    # AoC_07.test_abba("asdsdsda")
    # AoC_07.test_abba("abba")
    # AoC_07.test_abba("abbaasdabba")
    # AoC_07.test_abba("asdabba")
    # AoC_07.test_tls("asdqwe[asdqwe]asdqwe")
    # AoC_07.test_tls("assadqwe[asdqwe]asdqwe")
    # AoC_07.test_tls("qwassaqw[adda]addassa")
    # AoC_07.test_tls("asdqwe[asdaddaqwe]asdqwe")
    # AoC_07.test_tls("qwassaqw[asdqwe]addassa")
    # AoC_07.test_tls("qwassaqw[asdqwe]w")

    AoC_07.test_tls("abba[mnop]qrst")
    AoC_07.test_tls("abcd[bddb]xyyx")
    AoC_07.test_tls("aaaa[qwer]tyui")
    AoC_07.test_tls("ioxxoj[asdfgh]zxcvbn")


    solver = AoC_07()
    solver.run()
    exit(0)

