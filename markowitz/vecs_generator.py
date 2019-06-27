import numpy as np
import pandas as pd


def rasterize_barycentric(step):
    s = round(1/step, 4)
    points = list()

    for i in range(step+1):
        z = 1 - i*s
        xs = np.linspace(0, i*s, step)
        for x, y in zip(xs, i*s - xs):
            points.append((x, y, z))
    return points
