from __future__ import division
__author__ = 'mFoxRU'

import numpy as np
from abstractwavelet import AbstractWavelet


class Wave(AbstractWavelet):
    name = 'Wave'

    params = {
        'z1': {
            'min': .1,
            'max': 100,
            'def': 1
        },
        'z2': {
            'min': .1,
            'max': 100,
            'def': 2}
    }

    def fn(self):
        s = lambda a: 2 / (np.sqrt(3 * a) * (np.pi**0.25))
        v1 = lambda w: (np.arange(0, w) - (w - 1.0) / 2)
        v2 = lambda w: (np.arange(0, w) - (w - 1.0) / 2)**2
        z1, z2 = self.z1, self. z2
        return lambda w, a: (v1(w)/(v2(w)+z1**2) - v1(w)/(v2(w)+z2**2)) * s(a)
