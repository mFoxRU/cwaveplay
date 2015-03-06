__author__ = 'mFoxRU'

import scipy.signal as sps

from abstractwavelet import AbstractWavelet


class Ricker(AbstractWavelet):
    name = 'Ricker(MHAT)'
    params = {}

    def fn(self):
        return sps.ricker
