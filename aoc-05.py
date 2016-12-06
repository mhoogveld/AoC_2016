#!/usr/bin/python

import hashlib
from sys import hash_info

__author__ = "m.hoogveld@elevate.nl"

class AoC_05:
    def __init__(self):
        pass

    def run(self):
        door_id = "uqwqemis"
        passwd = dict()
        i = 0
        while len(passwd) < 8:
            hash_input = door_id + str(i)
            m = hashlib.md5()
            m.update(bytes(hash_input, 'ascii'))
            hex_md5 = (''.join(["%02X" % x for x in m.digest()]))
            if hex_md5.startswith('00000'):
                try:
                    pos = int(hex_md5[5])
                    if pos < 8:
                        if pos not in passwd:
                            passwd[pos] = hex_md5[6]
                            print("Found: {}".format(hex_md5[6]))
                except ValueError:
                    pass
            if i % 1000000 == 0:
                print("Round number: {}".format(i))
            i += 1

        print("Password for {} = {}".format(door_id, passwd))

if __name__ == "__main__":
    solver = AoC_05()
    solver.run()
    exit(0)

