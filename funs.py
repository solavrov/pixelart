from math import sin, cos, pi, exp, sqrt
from cmath import exp as c_exp


def pulsar(x, y, t, p):
    z = complex(x, y)
    d = complex(p["shift"]["x"], p["shift"]["y"])
    z = z * c_exp(complex(0, 1) * -p["omega"]["center"] * t)
    z = (z - d) * c_exp(complex(0, 1) * -p["omega"]["self"] * t) + d
    x = z.real
    y = z.imag
    return exp(-(cos(p["omega"]["pulse"] * t + p["phase"]) * (x - p["shift"]["x"]) / p["scale"]["x"]) ** 2 -
               (sin(p["omega"]["pulse"] * t + p["phase"]) * (y - p["shift"]["y"]) / p["scale"]["y"]) ** 2)