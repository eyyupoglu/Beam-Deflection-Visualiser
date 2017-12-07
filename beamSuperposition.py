# -*- coding: utf-8 -*-
"""
Beam Superposition Function
"""
#---------------------------Initialization-------------------------------------------------------------------------
import numpy as np
import math
from beamDeflection import *



def beamSuperposition(positions, beamLength, loadPositions, loadForces, beamSupport):
    #beamSuperposition(This does the same thing as beamDeflection (see beamDeflectionFunction) but it creates a superposition of 
    #beamdeflections for several loads in different positions at a time.)
    #Input      positions:(type: array of floats) All the different points along the beam where deflection
    #                     is being calculated for every elements of it.
    #           beamlength:(type: float)Length of the beam.(meter)
    #           loadPositions:(type: array of floats) The position of the loads from the very left point.
    #                       (meter)
    #           loadForces:(type: array of float) The magnitude of the loads.(kN)
    #           beamSupport:(type: integer)Numbers correlating to beam types.(1 for both end type,2 for 
    #                       cantilever)
    #Output     deflection:(type: array of floats) Deflections correlating to every points of the 
    #                       positions
    #                       vector.
    
    #defining an empty array for delfections
    deflections = np.zeros(len(positions))
    i = 0
    
    #filling the deflection array 
    for element in loadPositions:
        deflections = deflections + beamDeflection(positions, beamLength, element, loadForces[i], beamSupport)
        i = i + 1

