from Movie import Movie
from math import sin, cos, pi, exp, sqrt
from Clr import Clr
from numpy import array
from funs import pulsar

pulsar_params_1 = {

    "times": array(range(64)) / 2,
    "fps": 20,
    "w": 64,
    "h": 64,

    "pulsars": (

        {
            "scale": {"x": 8, "y": 8},
            "omega": {"pulse": 2 * pi / 32, "self": 2 * pi / 16, "center": 2 * pi / 32},
            "shift": {"x": 16, "y": 0},
            "phase": 0,
            "clr_min": Clr.k,
            "clr_max": Clr.g,
            "clr_mid": Clr.r
        },

        {
            "scale": {"x": 8, "y": 8},
            "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 2 * pi / 32},
            "shift": {"x": -16, "y": 0},
            "phase": 0,
            "clr_min": Clr.k,
            "clr_max": Clr.g,
            "clr_mid": Clr.r
        },

        {
            "scale": {"x": 8, "y": 8},
            "omega": {"pulse": 2 * pi / 32, "self": 2 * pi / 16, "center": 2 * pi / 32},
            "shift": {"x": 0, "y": 16},
            "phase": pi / 2,
            "clr_min": Clr.k,
            "clr_max": Clr.r,
            "clr_mid": Clr.b
        },

        {
            "scale": {"x": 8, "y": 8},
            "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 2 * pi / 32},
            "shift": {"x": 0, "y": -16},
            "phase": pi / 2,
            "clr_min": Clr.k,
            "clr_max": Clr.r,
            "clr_mid": Clr.b
        },

        {
            "scale": {"x": 8, "y": 8},
            "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 0},
            "shift": {"x": 0, "y": 0},
            "phase": 0,
            "clr_min": Clr.k,
            "clr_max": Clr.g,
            "clr_mid": Clr.r
        },

        {
            "scale": {"x": 8, "y": 8},
            "omega": {"pulse": 2 * pi / 32, "self": -2 * pi / 16, "center": 0},
            "shift": {"x": 0, "y": 0},
            "phase": pi / 2,
            "clr_min": Clr.k,
            "clr_max": Clr.r,
            "clr_mid": Clr.b
        }

    )

}


def produce_pulsar(params, file_name):
    movie = None
    for i, p in enumerate(params["pulsars"]):
        m = Movie(params["w"], params["h"], fps=params["fps"])
        m.shoot_func(lambda x, y, t: pulsar(x, y, t, p), params["times"],
                     clr_min=p["clr_min"], clr_max=p["clr_max"], clr_mid=p["clr_mid"])
        movie = m + movie
        print(str(i + 1) + " done!")
    movie.write_gif(file_name)
