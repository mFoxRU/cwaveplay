__author__ = 'mFoxRU'

import scipy.signal as sps

from abstractwavelet import AbstractWavelet


class Mhat(AbstractWavelet):
    params = {}

    def fn(self):
        return sps.ricker

    def name(self):
        return 'MHat'

