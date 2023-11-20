import re
from globals import WHICHWAY, WHEREAMI
import random
import collections
from src.dsDNA import Domain, Sequence
import math


def update_pos(pos, angle, distance):
    newpos = (0, 0)
    newpos = pos[0] + distance*math.cos(angle*math.pi/180), pos[1] + distance*math.sin(angle*math.pi/180)
    return newpos


def find_matching_leftb(domains, index):
    # Note that `domains[index]` should not contain left bracket
    ret = index - 1
    brackets = 0
    while ret >= 0:
        if domains[ret].is_leftb() and brackets==0:
            return ret
        if domains[ret].is_leftb():
            brackets += 1
        if domains[ret].is_rightb():
            brackets -= 1
        ret -= 1
    return ret


def find_best_direction(pos, occupied_xs=[], occupied_ys=[], offset=50):
    angles = [0, 90, 180, 270]
    for angle in angles:
        newpos = update_pos(pos, angle, offset)
        crosses = False
        for x in occupied_xs:
            if x > min(pos[0], newpos[0]) and x < max(pos[0], newpos[0]):
                crosses = True
                break
        for y in occupied_ys:
            if y > min(pos[1], newpos[1]) and y < max(pos[1], newpos[1]):
                crosses = True
                break
        if not crosses:
            return angle
    return 0


def parse_dsdna_sequence(domains: [Domain], whereami=WHEREAMI['BOTTOM'],
                         angle=0, startpos=(0, 0), **kwargs):

    main_stack = []  # Keeps track of the bound domains
    overhang_stack = []
    overhang_to_domain = None
    open_brackets_count = 0
    distance = 0  # Must be positive
    inside_overhang = True
    occupied_xs = []
    occupied_ys = []
    index = 0
    while index < len(domains):
        domain = domains[index] 
        print(domain)
        # If the domain contains a left bracket, simply add it to the stack.
        # Increase the bracket counter. 
        if domain.is_leftb():
            open_brackets_count += 1
            domain.angle = angle
            domain.distance = domain.length
            domain.startpos = startpos
            domain.whereami = whereami
            domain.endpos = update_pos(startpos, domain.angle, domain.distance)
            startpos = domain.endpos
            occupied_xs += [domain.startpos[0], domain.endpos[0]]
            occupied_ys += [domain.startpos[1], domain.endpos[1]]

        if domain.is_rightb():
            # Go back until you find a left bracket and value is zero.
            prev_leftb_index = find_matching_leftb(domains, index)
            compl_domain = domains[prev_leftb_index]
            domain.angle = (compl_domain.angle + 180) % 360
            domain.distance = compl_domain.distance
            domain.startpos = compl_domain.endpos
            domain.endpos = compl_domain.startpos
            domain.startpos = update_pos(domain.startpos, (angle+90)%360, 20)
            domain.endpos = update_pos(domain.endpos, (angle + 90)%360, 20)
            domain.whereami = -compl_domain.whereami
            open_brackets_count -= 1
            startpos = domain.endpos
                        
        if domain.is_overhang():
            # Change the angle by 90 in the appropriate direction
            offset = kwargs.get('overhang_offset', 20)
            angle = find_best_direction(startpos, occupied_xs, occupied_ys, offset)
            startpos = update_pos(startpos, angle, distance=2*offset)
            angle = (angle + 180)%360
            domain.distance = domain.length
            domain.angle = angle 
            domain.startpos = startpos

        index += 1
    return domains
