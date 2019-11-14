import numpy as np


def initialize():
    global feature_arr
    feature_arr = np.zeros([2983, 12])
    global labels
    labels = []
    global a
    a = np.zeros([0, 1500, 6])