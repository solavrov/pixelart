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
from random import uniform


class Root:

    def __init__(self, value, power, rotate, phi=0.0):
        self.value = value
        self.power = power
        self.rot = rotate
        self.phi = phi


class Studio1:

    def __init__(self,
                 w=128,
                 h=128,
                 times=array(range(60)),
                 fps=20,
                 omega=2 * pi / 60,
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

    def append_root(self, root, power, rotate):
        self.roots.append(Root(root, power, rotate))
        return self

    def set_num_of_frames(self, n):
        self.times = array(range(n))
        self.omega = 2 * pi / n

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
            print("producing! please, wait...")
            m = Movie(self.w, self.h, fps=self.fps)
            m.shoot_func(self.func, self.times, clr_min=self.clr_min, clr_max=self.clr_max, clr_mid=self.clr_mid)
            m.write_gif(filename)
            print("done!")

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

    def make_rand_roots_inf(self, n):
        self.roots = []
        for _ in range(n):
            phi = uniform(0, 2 * pi)
            v = complex(cos(phi), sin(phi) * cos(phi)) * 3 / 4
            self.roots.append(Root(v, choice(self.pow_set), choice(self.rot_set), phi))

    def rotate_roots_inf(self, t):
        if len(self.roots) == 0:
            sys.exit("rotate_roots: no roots")
        else:
            rotated_roots = []
            for r in self.roots:
                phi = r.phi + r.rot * self.omega * t
                v = complex(cos(phi), sin(phi) * cos(phi)) * 3 / 4
                rotated_roots.append(Root(v, r.power, r.rot, phi))
            return rotated_roots

    def make_func_inf(self):
        if len(self.roots) == 0:
            sys.exit("make_func: no roots")
        else:

            def f(x, y, t):
                z = complex(x / (self.w / 2), y / (self.h / 2))
                roots = self.rotate_roots_inf(t)
                zz = 1
                for r in roots:
                    zz *= (z - r.value) ** r.power
                return abs(arg(zz))

            self.func = f

    def produce_rand_inf(self, num_of_roots, filename):
        self.make_rand_roots_inf(num_of_roots)
        self.make_func_inf()
        self.produce(filename)
