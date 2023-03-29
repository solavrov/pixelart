from Movie import Movie
from Frame import Frame
from math import sin, cos, pi, exp, sqrt
from cmath import exp as c_exp
from cmath import phase as arg
from Clr import Clr
from numpy import array
from random import randrange as rnd


def f1(x, y, t):
    a = b = 64 - 8
    c = 2 * pi / 32
    z = complex(x / a, y / b)
    return abs(cos(c * t) * (z ** 3 + 1j) + sin(c * t) * z * 2.5)


def f2(x, y, t):
    a = b = 64
    c = 2 * pi / 32
    z = complex(x / a, y / b)
    r1 = c_exp(pi / 2 * 1j + 0 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r2 = c_exp(pi / 2 * 1j + 1 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r3 = c_exp(pi / 2 * 1j + 2 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r4 = c_exp(pi / 2 * 1j + 3 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r5 = c_exp(pi / 2 * 1j + 4 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    return abs((z - r1) * (z - r2) * (z - r3) * (z - r4) * (z - r5))


def f3(x, y, t):
    a = b = 64 - 8
    c = 2 * pi / 32
    z = complex(x / a, y / b)
    return arg((cos(c * t) * (z ** 3 + 1j) + sin(c * t) * z * 2.5))


def f4(x, y, t):
    a = b = 64
    c = 2 * pi / 32
    z = complex(x / a, y / b)
    r1 = c_exp(pi / 2 * 1j + 0 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r2 = c_exp(pi / 2 * 1j + 1 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r3 = c_exp(pi / 2 * 1j + 2 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r4 = c_exp(pi / 2 * 1j + 3 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r5 = c_exp(pi / 2 * 1j + 4 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    return arg((z - r1) * (z - r2) * (z - r3) * (z - r4) * (z - r5))


def f5(x, y, t):
    a = b = 64
    c = 2 * pi / 32
    c2 = c * 2
    z = complex(x / a, y / b)
    z = z * c_exp(1j * c2 * t)
    r1 = c_exp(pi / 2 * 1j + 0 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r2 = c_exp(pi / 2 * 1j + 1 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r3 = c_exp(pi / 2 * 1j + 2 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r4 = c_exp(pi / 2 * 1j + 3 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    r5 = c_exp(pi / 2 * 1j + 4 * 2 * pi / 5 * 1j) * (cos(c * t) ** 1)
    return arg((z - r1) * (z - r2) * (z - r3) * (z - r4) * (z - r5))


def get_rand_roots(n):
    roots = []
    for _ in range(n):
        roots.append((rnd(-200, 201) + rnd(-200, 201) * 1j) / 100)
    return roots


def rotate_roots(roots, omega, t):
    r = []
    for i in range(0, len(roots)):
        r.append(roots[i] * c_exp(((-1) ** i) * 1j * omega * t))
    return r


def gen_fun(num_roots):
    roots = get_rand_roots(num_roots)

    def f(x, y, t):
        a = b = 64 - 8
        c = 2 * pi / 32
        z = complex(x / a, y / b)
        rotated_roots = rotate_roots(roots, c, t)
        zz = 1
        for r in rotated_roots:
            zz *= (z - r)
        return abs(arg(zz))

    return f


def produce_complex(f, file_name):
    times = array(range(64)) / 2
    m = Movie(w=128, h=128, fps=20)
    m.shoot_func(f, times, clr_min=Clr.g, clr_max=Clr.r, clr_mid=Clr.b)
    m.write_gif(file_name)
