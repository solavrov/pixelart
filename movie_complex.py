from Movie import Movie
from Frame import Frame
from math import sin, cos, pi, exp, sqrt, log
from cmath import exp as c_exp
from cmath import phase as arg
from Clr import Clr
from numpy import array
from random import randrange as rnd
from random import choice

default_complex_params = {
    "w": 128,
    "h": 128,
    "times": array(range(64)),
    "fps": 20,
    "omega": 2 * pi / 64
}


def get_rand_roots(n):
    values = []
    powers = []
    for _ in range(n):
        values.append((rnd(-100, 100) + rnd(-100, 101) * 1j) / 111)
        powers.append(choice([-3, -2, -1, 1, 2, 3]))
    return {"val": values, "pow": powers}


def rotate_roots(roots, params, t):
    r = []
    for i in range(len(roots["val"])):
        r.append(roots["val"][i] * c_exp(((-1) ** i) * 1j * params["omega"] * t))
    return {"val": r, "pow": roots["pow"]}


def gen_fun(num_roots, params):
    roots = get_rand_roots(num_roots)
    print(roots)

    def f(x, y, t):
        a = params["w"] / 2
        b = params["h"] / 2
        c = params["omega"]
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
