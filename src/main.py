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
# end imports

# begin code

def get_args():
    parser = argparse.ArgumentParser("Arguments.")


    args = parser.parse_args()
    return args





if __name__=="__main__":
    opt = get_args()

