from __future__ import division
__author__ = 'mFoxRU'

import numpy as np
from abstractwavelet import AbstractWavelet


class Spike(AbstractWavelet):
    name = 'Spike'

    params = {
        'z1': {
            'min': 0,
            'max': 100,
            'def': 1
        },
        'z2': {
            'min': 0,
            'max': 100,
            'def': 2}
    }

    def fn(self):
        s = lambda a: 2 / (np.sqrt(3 * a) * (np.pi**0.25))
        v2 = lambda w: (np.arange(0, w) - (w - 1.0) / 2)**2
        z1, z2 = self.z1, self. z2
        return lambda w, a: (z1/(v2(w)+z1**2) - z2/(v2(w)+z2**2)) * s(a)
