__author__ = 'mFoxRU'

from ricker import Ricker
from spike import Spike
from wave import Wave

wavelets_dic = {
    w.name: w for w in (Ricker, Spike, Wave)
}