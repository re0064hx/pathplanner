import numpy as np

def calc_refpath():
    x = np.zeros((k_num, 1))
    y = np.zeros((k_num, 1))
    rho = 1/500
    R = 1/rho
    theta = np.arange(0, math.pi, 0.1)

    x = R * np.cos(theta) - R
    y = R * np.sin(theta)

    return x, y