#!/usr/bin/python

import re

__author__ = "m.hoogveld@elevate.nl"

class AoC_10:
    def __init__(self):
        self.bots = dict()
        self.outputs = dict()

    def run(self):
        input_file = 'input-10'
        with open(input_file, 'r', encoding='utf-8') as infile:
            for line in infile:
                self.process_instr(line.strip())

        print(self.outputs[0].chips[0] * self.outputs[1].chips[0] * self.outputs[2].chips[0])

    def process_instr(self, instr):
        if instr.startswith("bot"):
            bot_re = r"bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)"
            bot_match = re.match(bot_re, instr)

            from_bot_id = int(bot_match.group(1))
            low_type = bot_match.group(2)
            low_id = int(bot_match.group(3))
            high_type = bot_match.group(4)
            high_id = int(bot_match.group(5))

            from_bot = self.get_dest("bot", from_bot_id)
            low_dest = self.get_dest(low_type, low_id)
            high_dest = self.get_dest(high_type, high_id)

            self.add_bot_instr(from_bot, low_dest, high_dest)

        elif instr.startswith("value"):
            value_instr_re = r"value (\d+) goes to bot (\d+)"
            value_instr_match = re.match(value_instr_re, instr)
            chip_value = int(value_instr_match.group(1))
            chip_dest = self.get_dest("bot", int(value_instr_match.group(2)))
            self.add_chip_dest(chip_value, chip_dest)

    def add_bot_instr(self, from_bot, low_dest, high_dest):
        from_bot.lower_dest = low_dest
        from_bot.higher_dest = high_dest
        from_bot.try_distribute()

    def add_chip_dest(self, chip_value, chip_dest):
        chip_dest.add_chip(chip_value)
        chip_dest.try_distribute()

    def get_dest(self, dest_type, dest_id):
        if dest_type == "bot":
            return self.get_or_init_bot(dest_id)
        elif dest_type == "output":
            return self.get_or_init_output(dest_id)

    def get_or_init_bot(self, bot_id):
        if bot_id not in self.bots:
            bot = Bot()
            bot.id = bot_id
            self.bots[bot_id] = bot
        else:
            bot = self.bots.get(bot_id)

        return bot

    def get_or_init_output(self, output_id):
        if output_id not in self.outputs:
            output = Output()
            output.id = output_id
            self.outputs[output_id] = output
        else:
            output = self.outputs.get(output_id)

        return output


class Bot:
    MAX_CHIPS = 2
    MY_TYPE = "Bot"

    def __init__(self):
        self.id = None
        self.chips = []
        self.lower_dest = None
        self.higher_dest = None
        self.distributed = False

    def add_chip(self, value):
        if len(self.chips) == self.MAX_CHIPS:
            raise Exception("No room for an other chip for bot {}".format(self.id))
        self.chips.append(value)

    def try_distribute(self):
        if not self.distributed and len(self.chips) == self.MAX_CHIPS and self.lower_dest and self.higher_dest:
            if self.chips[0] > self.chips[1]:
                lower_chip = self.chips[1]
                higher_chip = self.chips[0]
            else:
                lower_chip = self.chips[0]
                higher_chip = self.chips[1]

            self.lower_dest.add_chip(lower_chip)
            self.higher_dest.add_chip(higher_chip)

            print("Bot {} compares chips {} and {}".format(self.id, lower_chip, higher_chip))
            if lower_chip == 17 and higher_chip == 61:
                print("*** This is the bot we are looking for")

            self.distributed = True

            if self.lower_dest.MY_TYPE == "Bot":
                self.lower_dest.try_distribute()
            if self.higher_dest.MY_TYPE == "Bot":
                self.higher_dest.try_distribute()


class Output:
    MY_TYPE = "Output"

    def __init__(self):
        self.id = None
        self.chips = []

    def add_chip(self, value):
        self.chips.append(value)


if __name__ == "__main__":
    solver = AoC_10()
    solver.run()
    exit(0)

