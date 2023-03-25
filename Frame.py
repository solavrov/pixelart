from numpy import array, empty
from Clr import Clr
from array2gif import write_gif


class Frame:

    def __init__(self, w=32, h=32, bg_color=Clr.k):
        self.w = w
        self.h = h
        self.canvas = empty((h, w), dtype=object)
        self.canvas.fill(bg_color)

    def slice(self):
        red, green, blue = [], [], []
        for line in self.canvas:
            red_line, green_line, blue_line = [], [], []
            for p in line:
                red_line.append(p[0])
                green_line.append(p[1])
                blue_line.append(p[2])
            red.append(red_line)
            green.append(green_line)
            blue.append(blue_line)
        return array([red, green, blue])

    def write_gif(self, filename):
        write_gif(self.slice(), filename + '.gif')

    def draw_dot(self, x, y, color):
        self.canvas[x % self.w, y % self.h] = color

    def draw_func(self, func, t=None, z_min=None, z_max=None, clr_min=Clr.b, clr_max=Clr.r, clr_mid=Clr.g):
        z = empty((self.h, self.w))
        for y in range(self.h):
            for x in range(self.w):
                if t is None:
                    z[y, x] = func(x - (self.w - 1) / 2, -y + (self.h - 1) / 2)
                else:
                    z[y, x] = func(x - (self.w - 1) / 2, -y + (self.h - 1) / 2, t)
        if z_min is None:
            z_min = z.min()
        if z_max is None:
            z_max = z.max()
        for y in range(self.h):
            for x in range(self.w):
                self.canvas[x, y] = Clr.get(z[x, y], z_min, z_max, clr_min, clr_max, clr_mid)

    def __add__(self, other):
        f = Frame(self.w, self.h)
        for k, line in enumerate(self.canvas):
            for i, d in enumerate(line):
                f.canvas[k, i] = Clr.sum(d, other.canvas[k, i], sum_type=1)
        return f

    def __mul__(self, other):
        f = Frame(self.w, self.h)
        for k, line in enumerate(self.canvas):
            for i, d in enumerate(line):
                f.canvas[k, i] = Clr.sum(d, other.canvas[k, i], sum_type=2)
        return f

    def __mod__(self, other):
        f = Frame(self.w, self.h)
        for k, line in enumerate(self.canvas):
            for i, d in enumerate(line):
                f.canvas[k, i] = Clr.sum(d, other.canvas[k, i], sum_type=3)
        return f






