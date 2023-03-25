from Movie import Movie
from math import sin, cos, pi, exp, sqrt
from Clr import Clr
from numpy import array
from funs import pulsar


def produce_pulsar(file_name="pulsar"):
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
    print("1 done!")

    m2 = Movie(fps=20, w=w, h=h)
    m2.shoot_func(f2, time, clr_min=Clr.k, clr_max=Clr.g, clr_mid=Clr.r)
    print("2 done!")

    m3 = Movie(fps=20, w=w, h=h)
    m3.shoot_func(f3, time, clr_min=Clr.k, clr_max=Clr.r, clr_mid=Clr.b)
    print("3 done!")

    m4 = Movie(fps=20, w=w, h=h)
    m4.shoot_func(f4, time, clr_min=Clr.k, clr_max=Clr.r, clr_mid=Clr.b)
    print("4 done!")

    m5 = Movie(fps=20, w=w, h=h)
    m5.shoot_func(f5, time, clr_min=Clr.k, clr_max=Clr.g, clr_mid=Clr.r)
    print("5 done!")

    m6 = Movie(fps=20, w=w, h=h)
    m6.shoot_func(f6, time, clr_min=Clr.k, clr_max=Clr.r, clr_mid=Clr.b)
    print("6 done!")

    m = m1 + m2 + m3 + m4 + m5 + m6

    m.write_gif(file_name)
