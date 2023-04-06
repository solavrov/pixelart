from Clr import Clr
from math import sin, cos, pi, exp, sqrt, log
from cmath import exp as c_exp
from Studio1 import Studio1

s = Studio1()

# r1 = 2 / 3 * c_exp(1j * 1 / 6 * 2 * pi)
# r2 = 2 / 3 * c_exp(1j * 2 / 6 * 2 * pi)
# r3 = 2 / 3 * c_exp(1j * 3 / 6 * 2 * pi)
# r4 = 2 / 3 * c_exp(1j * 4 / 6 * 2 * pi)
# r5 = 2 / 3 * c_exp(1j * 5 / 6 * 2 * pi)
# r6 = 2 / 3 * c_exp(1j * 6 / 6 * 2 * pi)
#
# s.append_root(r1, 1, 2).append_root(r2, 1, 2).append_root(r3, 1, 2)
# s.append_root(r4, 1, 2).append_root(r5, 1, 2).append_root(r6, 1, 2)
# s.make_func()
# s.produce_frame(0, "frameX")
# s.produce("complex8")

s.produce_rand_inf(10, "complex_inf_1")


