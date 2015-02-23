from __future__ import division

import numpy as np

def lorentzian(x, x0, A, gamma):
    return A / (np.pi*gamma*(1 + ((x - x0)/gamma)**2))

# ... code that uses the `lorentzian` to fit a spectral line goes here ...
