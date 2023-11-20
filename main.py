"""
Filename: main.py

Author: rajiv256

Created on: 13-11-2023

Description:
"""

# begin imports
import os
import sys
import random
import seaborn as sns
import argparse
import logging
import pickle as pkl

from tqdm import tqdm
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data.dataset import Dataset
from utils import parse_dsdna_sequence
from src.dsDNA import Domain, Sequence
from src.dnaturtle import DNATurtle
import turtle

# end imports

# begin code

def get_args():
    parser = argparse.ArgumentParser("Arguments.")


    args = parser.parse_args()
    return args





if __name__=="__main__":
    opt = get_args()
    notation = "sC mC fC( hCk( + sC mC fC( hCj( + fB* ) ) ) )"
    seq = Sequence(seq=notation)
    domains = parse_dsdna_sequence(seq.domains)
    

    dt = DNATurtle()
    for domain in domains:
        dt.draw_domain(domain)
    turtle.mainloop()
