from Movie import Movie
from math import sin, cos, pi, exp, sqrt
from cmath import exp as c_exp
from Clr import Clr
from numpy import array


def pulsar(x, y, t, p):
    z = complex(x, y)
    d = complex(p["shift"]["x"], p["shift"]["y"])
    z = z * c_exp(complex(0, 1) * -p["omega"]["center"] * t)
    z = (z - d) * c_exp(complex(0, 1) * -p["omega"]["self"] * t) + d
    x = z.real
    y = z.imag
    return exp(-(cos(p["omega"]["pulse"] * t + p["phase"]) * (x - p["shift"]["x"]) / p["scale"]["x"]) ** 2 -
               (sin(p["omega"]["pulse"] * t + p["phase"]) * (y - p["shift"]["y"]) / p["scale"]["y"]) ** 2)


def f1(x, y, t):
    p = {
        "scale": {"x": 8, "y": 8},
        "omega": {"pulse": 2 * pi / 32, "self": 2 * pi / 16, "center": 2 * pi / 32},
        "shift": {"x": 16, "y": 0},
        "phase": 0
    }
    return pulsar(x, y, t, p)


def f2(x, y, t):
    p = {
        "scale": {"x": 8, "y": 8},
        "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 2 * pi / 32},
        "shift": {"x": -16, "y": 0},
        "phase": 0
    }
    return pulsar(x, y, t, p)


def f3(x, y, t):
    p = {
        "scale": {"x": 8, "y": 8},
        "omega": {"pulse": 2 * pi / 32, "self": 2 * pi / 16, "center": 2 * pi / 32},
        "shift": {"x": 0, "y": 16},
        "phase": pi / 2
    }
    return pulsar(x, y, t, p)


def f4(x, y, t):
    p = {
        "scale": {"x": 8, "y": 8},
        "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 2 * pi / 32},
        "shift": {"x": 0, "y": -16},
        "phase": pi / 2
    }
    return pulsar(x, y, t, p)


def f5(x, y, t):
    p = {
        "scale": {"x": 8, "y": 8},
        "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 0},
        "shift": {"x": 0, "y": 0},
        "phase": 0
    }
    return pulsar(x, y, t, p)


def f6(x, y, t):
    p = {
        "scale": {"x": 8, "y": 8},
        "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 0},
        "shift": {"x": 0, "y": 0},
        "phase": pi / 2
    }
    return pulsar(x, y, t, p)


time = array(range(64)) / 2

w = h = 64

m1 = Movie(fps=20, w=w, h=h)
m1.shoot_func(f1, time, clr_min=Clr.k, clr_max=Clr.g, clr_mid=Clr.r)
print("1 done!\n")

m2 = Movie(fps=20, w=w, h=h)
m2.shoot_func(f2, time, clr_min=Clr.k, clr_max=Clr.g, clr_mid=Clr.r)
print("2 done!\n")

m3 = Movie(fps=20, w=w, h=h)
m3.shoot_func(f3, time, clr_min=Clr.k, clr_max=Clr.r, clr_mid=Clr.b)
print("3 done!\n")

m4 = Movie(fps=20, w=w, h=h)
m4.shoot_func(f4, time, clr_min=Clr.k, clr_max=Clr.r, clr_mid=Clr.b)
print("4 done!\n")

m5 = Movie(fps=20, w=w, h=h)
m5.shoot_func(f5, time, clr_min=Clr.k, clr_max=Clr.g, clr_mid=Clr.r)
print("5 done!\n")

m6 = Movie(fps=20, w=w, h=h)
m6.shoot_func(f6, time, clr_min=Clr.k, clr_max=Clr.r, clr_mid=Clr.b)
print("6 done!\n")

m = m1 + m2 + m3 + m4 + m5 + m6

m.write_gif('m4')
