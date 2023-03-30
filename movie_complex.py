from Movie import Movie
from Frame import Frame
from math import sin, cos, pi, exp, sqrt, log
from cmath import exp as c_exp
from cmath import phase as arg
from Clr import Clr
from numpy import array
from random import randrange as rnd
from random import choice


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


def f6(x, y, t):
    a = b = 64
    c = 2 * pi / 32
    z = complex(x / a, y / b)
    roots = rotate_roots([0.5176768, 0.497876876 * 1j, -0.47997234, -0.529823287 * 1j], c, t)
    zz = 1
    for i, r in enumerate(roots):
        zz *= (z - r) ** ((-1) ** i)
    return abs(arg(zz))


def get_rand_roots(n):
    values = []
    powers = []
    for _ in range(n):
        values.append((rnd(-100, 100) + rnd(-100, 101) * 1j) / 111)
        powers.append(choice([-3, -2, -1, 1, 2, 3]))
    return {"val": values, "pow": powers}


def rotate_roots(roots, omega, t):
    r = []
    for i in range(len(roots["val"])):
        r.append(roots["val"][i] * c_exp(((-1) ** i) * 1j * omega * t))
    return {"val": r, "pow": roots["pow"]}


def gen_fun(num_roots):
    roots = get_rand_roots(num_roots)
    print(roots)

    def f(x, y, t):
        a = b = 64
        c = 2 * pi / 32
        z = complex(x / a, y / b)
        rot_roots = rotate_roots(roots, c, t)
        zz = 1
        for i in range(len(rot_roots["val"])):
            zz *= (z - rot_roots["val"][i]) ** rot_roots["pow"][i]
        return abs(arg(zz))

    return f


def produce_complex(f, file_name):
    times = array(range(64)) / 2
    m = Movie(w=128, h=128, fps=20)
    m.shoot_func(f, times, clr_min=Clr.g, clr_max=Clr.r, clr_mid=Clr.b)
    m.write_gif(file_name)
