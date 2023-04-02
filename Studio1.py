import sys
from Movie import Movie
from Frame import Frame
from math import sin, cos, pi, exp, sqrt, log
from cmath import exp as c_exp
from cmath import phase as arg
from Clr import Clr
from numpy import array
from random import randrange as rnd
from random import choice


class Root:

    def __init__(self, value, power, rot):
        self.value = value
        self.power = power
        self.rot = rot


class Studio1:

    def __init__(self,
                 w=128,
                 h=128,
                 times=array(range(64)),
                 fps=20,
                 omega=2 * pi / 64,
                 pow_set=(-3, -2, -1, 1, 2, 3),
                 rot_set=(-1, 1),
                 clr_min=Clr.g,
                 clr_max=Clr.r,
                 clr_mid=Clr.b
                 ):

        self.w = w
        self.h = h
        self.times = times
        self.fps = fps
        self.omega = omega
        self.pow_set = pow_set
        self.rot_set = rot_set
        self.clr_min = clr_min
        self.clr_max = clr_max
        self.clr_mid = clr_mid
        self.roots: [Root] = []
        self.func = None

    def append_root(self, root, power, rot):
        self.roots.append(Root(root, power, rot))
        return self

    def make_rand_roots(self, n):
        self.roots = []
        for _ in range(n):
            self.roots.append(Root((rnd(-100, 100) + rnd(-100, 101) * 1j) / 111,
                                   choice(self.pow_set), choice(self.rot_set)))

    def rotate_roots(self, t):
        if len(self.roots) == 0:
            sys.exit("rotate_roots: no roots")
        else:
            rotated_roots = []
            for r in self.roots:
                rotated_roots.append(Root(r.value * c_exp(r.rot * 1j * self.omega * t), r.power, r.rot))
            return rotated_roots

    def make_func(self):
        if len(self.roots) == 0:
            sys.exit("make_func: no roots")
        else:

            def f(x, y, t):
                z = complex(x / (self.w / 2), y / (self.h / 2))
                roots = self.rotate_roots(t)
                zz = 1
                for r in roots:
                    zz *= (z - r.value) ** r.power
                return abs(arg(zz))

            self.func = f

    def produce(self, filename):
        if self.func is None:
            sys.exit("produce: no fun")
        else:
            m = Movie(self.w, self.h, fps=self.fps)
            m.shoot_func(self.func, self.times, clr_min=self.clr_min, clr_max=self.clr_max, clr_mid=self.clr_mid)
            m.write_gif(filename)

    def produce_rand(self, num_of_roots, filename):
        self.make_rand_roots(num_of_roots)
        self.make_func()
        self.produce(filename)

    def produce_frame(self, frame_number, filename):
        if self.func is None:
            sys.exit("produce: no fun")
        else:
            frame = Frame(self.w, self.h)
            frame.draw_func(self.func, self.times[frame_number],
                            clr_min=self.clr_min, clr_max=self.clr_max, clr_mid=self.clr_mid)
            frame.write_gif(filename)
