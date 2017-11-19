import numpy as np

import math

from beamDeflection import *



def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    deflections = np.zeros(len(positions))
    i = 0
    for element in loadPositions:
        deflections = deflections + beamDeflection(positions, beamLength, element, loadForces[i], beamSupport)
        i = i + 1
    return deflections

test_1 = beamDeflection(positions, beam_length, beam_length/2,  100, 1)

