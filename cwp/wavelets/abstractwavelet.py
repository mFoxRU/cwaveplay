__author__ = 'mFoxRU'

import abc


class AbstractWavelet(object):
    __metaclass__ = abc.ABCMeta

    name = "This is my name"
    params = {
        'q': {  # Parameter Variable Name
            'min': 0,    # Minimal Variable Value (int/float)
            'max': 100,  # Maximal Variable Value (int/float)
            'def': 20    # Default Variable Value (int/float)
        }
    }

    def __init__(self, points=201):
        self.a = 1
        self.p = points
        for p, values in self.params.iteritems():
            if p not in vars(self):
                vars(self)[p] = values['def']
            else:
                raise KeyError('Variable "{}" already in use'.format(p))

    def set_window(self, value):
        if value > 0:
            self.p = value

    def set_scale(self, value):
        self.a = value

    def change_param(self, param, value):
        if param in self.params:
            if self.params[param]['min'] < value < self.params[param]['max']:
                vars(self)[param] = value

    @property
    def vector(self):
        return self.fn()(self.p, self.a)

    @abc.abstractmethod
    def fn(self):
        q = self.q
        return lambda a, w: NotImplementedError