#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_04:
    def __init__(self):
        pass

    def run(self):
        room_input_file = "input-04"
        room_count = self.count_valid_rooms(room_input_file)

        print("Number of rooms: {}".format(room_count))

    def count_valid_rooms(self, input_file):
        room_count = 0
        sector_id_sum = 0
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                room_def_match = re.match("([a-z\-]+)(\d+)\[([a-z]+)\]", line)
                if room_def_match:
                    words = room_def_match.group(1)
                    sector_id = int(room_def_match.group(2))
                    room_hash = room_def_match.group(3)

                    if self.is_valid_room(words, room_hash):
                        room_name = self.decrypt_room_name(words, sector_id)
                        if room_name.find('north') != -1:
                            print(room_name + ' ' + str(sector_id))
                        sector_id_sum += sector_id
        return sector_id_sum

    @staticmethod
    def is_valid_room(words, hash_provided):
        char_count = dict()
        hash_calculated = ""

        for char in words:
            if char == '-':
                continue
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1

        hash_dict = dict()
        for k, v in char_count.items():
            if v in hash_dict:
                hash_dict[v].append(k)
            else:
                hash_dict[v] = [k]

        for k in sorted(hash_dict.keys(), reverse=True):
            hash_calculated += ''.join(sorted(hash_dict[k]))

        hash_calculated = hash_calculated[:5]

        return hash_provided == hash_calculated

    @staticmethod
    def decrypt_room_name(crypt_text, shift_count):
        plain_text = ""
        alphabet_size = 26
        shift_count %= alphabet_size
        max_ord = ord('z')
        for char in crypt_text:
            if char == '-':
                plain_text += '-'
                continue
            new_ord = ord(char) + shift_count
            if new_ord > max_ord:
                new_ord -= alphabet_size
            plain_text += chr(new_ord)

        return plain_text

if __name__ == "__main__":
    solver = AoC_04()
    solver.run()
    exit(0)

