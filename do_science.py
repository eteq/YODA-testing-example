from __future__ import division

import numpy as np

def lorentzian(x, x0, A, gamma):
    return A / (gamma*(1 + ((x - x0)/gamma)**2))
