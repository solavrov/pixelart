from array2gif import write_gif
from Frame import Frame
from Clr import Clr
from numpy import empty


class Movie:

    def __init__(self, w=32, h=32, bg_color=Clr.k, fps=5):
        self.film = []
        self.w = w
        self.h = h
        self.bg_color = bg_color
        self.fps = fps

    def add_frame(self, frame):
        self.film.append(frame)

    def get_func_min_max(self, func, times):
        z = empty((len(times), self.h, self.w))
        for i, t in enumerate(times):
            for y in range(self.h):
                for x in range(self.w):
                    z[i, y, x] = func(x - (self.w - 1) / 2, -y + (self.h - 1) / 2, t)
        return z.min(), z.max()

    def shoot_func(self, func, times, z_min=None, z_max=None, clr_min=Clr.b, clr_max=Clr.r, clr_mid=Clr.g):
        if z_min or z_max is None:
            mm = self.get_func_min_max(func, times)
            if z_min is None:
                z_min = mm[0]
            if z_max is None:
                z_max = mm[1]
        for t in times:
            f = Frame(self.w, self.h, self.bg_color)
            f.draw_func(func, t, z_min, z_max, clr_min, clr_max, clr_mid)
            self.add_frame(f)

    def slice(self):
        s = []
        for f in self.film:
            s.append(f.slice())
        return s

    def write_gif(self, filename):
        write_gif(self.slice(), filename + '.gif', self.fps)

    def write_frames(self, filename):
        f: Frame
        for i, f in enumerate(self.film):
            f.write_gif(filename + str(i))

    def __add__(self, other):
        if other is None:
            return self
        m = Movie(self.w, self.h, fps=self.fps)
        for i, f in enumerate(self.film):
            m.add_frame(f + other.film[i])
        return m

    def __mul__(self, other):
        m = Movie(self.w, self.h, fps=self.fps)
        for i, f in enumerate(self.film):
            m.add_frame(f * other.film[i])
        return m

    def __mod__(self, other):
        m = Movie(self.w, self.h, fps=self.fps)
        for i, f in enumerate(self.film):
            m.add_frame(f % other.film[i])
        return m
