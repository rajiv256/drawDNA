import re
from globals import WHEREAMI, WHICHWAY, DOMAIN_PATTERN, PUNCT


class Domain:
    def __init__(self, label='fC', color='black', length=20, width=3, angle=0,
                 whereami=WHEREAMI['TOP'],
                 whichway=WHICHWAY['RIGHT2LEFT'],
                 startpos=(0, 0), endpos=(0, 10)):
        x = 2
        self.label = label
        self.color = color
        self.length = length
        self.width = width
        self.whereami = whereami
        self.angle = 0  # Need to be set
        self.startpos = (0, 0)  # Need to be set
        self.distance = 20  # Need to be set

    @staticmethod
    def _assign_color():
        return 'black'

    def is_overhang(self):
        return PUNCT['LEFTB'] not in self.label \
               or PUNCT['RIGHTB'] not in self.label \
                or PUNCT['PLUS'] not in self.label

    def is_plus(self):
        return PUNCT['PLUS'] in self.label

    def is_leftb(self):
        return PUNCT['LEFTB'] in self.label

    def is_rightb(self):
        return PUNCT['RIGHTB'] in self.label

    def __str__(self):
        return f'{self.label}({self.length})({self.whereami})'


class Sequence:
    def __init__(self, seq: str = 'hCj sC mC fC'):
        self.seq = seq
        list_of_strs = re.findall(DOMAIN_PATTERN, seq)
        self.domains = [Domain(label=s) for s in list_of_strs]



