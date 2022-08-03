import argparse
import torch
import random
import numpy as np
import wandb
from munch import DefaultMunch
import sys


def seed_all(seed):
    seed = int(seed)
    torch.manual_seed(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False
