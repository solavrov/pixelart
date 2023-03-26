from Movie import Movie
from Frame import Frame
from math import sin, cos, pi, exp, sqrt
from cmath import exp as c_exp
from Clr import Clr
from numpy import array


def f(x, y, t):
    a = b = 64 - 8
    c = 2 * pi / 32
    z = complex(x / a, y / b)
    return abs(cos(c * t) * (z ** 3 + 1j) + sin(c * t) * z * 2.5)


def produce_complex(file_name):
    times = array(range(64)) / 2
    m = Movie(w=128, h=128, fps=20)
    m.shoot_func(f, times, clr_min=Clr.g, clr_max=Clr.r, clr_mid=Clr.b)
    m.write_gif(file_name)
