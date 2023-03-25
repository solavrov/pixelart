from numpy import array, round


class Clr:
    r = array([255, 0, 0])
    g = array([0, 255, 0])
    b = array([0, 0, 255])
    k = array([0, 0, 0])
    w = array([255, 255, 255])

    @staticmethod
    def get(z, z_min, z_max, clr_min, clr_max, clr_mid):
        if clr_mid is None:
            clr_mid = round((clr_min + clr_max) / 2).astype(int)
        z = (z - z_min) / (z_max - z_min)
        z = round(255 * z) / 255
        if z <= 0:
            c = clr_min
        elif z <= 0.5:
            c = clr_min * (1 - 2 * z) + clr_mid * 2 * z
        elif z <= 1:
            c = clr_mid * 2 * (1 - z) + clr_max * (2 * z - 1)
        else:
            c = clr_max
        return round(c).astype(int)

    @staticmethod
    def sum(c1: array, c2: array, sum_type) -> array:
        if sum_type == 1:
            c = (c1 + c2)
            for i, m in enumerate(c):
                if m > 255:
                    c[i] = 255
        elif sum_type == 2:
            c = round((c1 + c2) / 2).astype(int)
        elif sum_type == 3:
            c = (c1 + c2) % 256
        else:
            c = Clr.w
        return Clr.round(c)

    @staticmethod
    def round(c):
        rg_rounds = [0, 51, 102, 153, 204, 255]
        b_rounds = [0, 42, 85, 128, 170, 213, 255]
        r = rg_rounds[c[0] // 43]
        g = rg_rounds[c[1] // 43]
        b = b_rounds[c[2] // 37]
        return array([r, g, b])











