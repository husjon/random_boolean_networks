import random


class TruthTable(dict):
    def __init__(self, dimentions):
        super().__init__(self)
        max_input = 2**dimentions

        padding = len(bin(max_input-1)[2:])
        for i in range(max_input):
            _input = str(i).rjust(padding, '0')
            self[i] = {
                'input': _input,
                'value': random.randint(0, 1)
            }
