# -*- coding: utf-8 -*-
"""
BeamDeflectionFunction
"""
import numpy as np


#These are the constant values corresponding to material of beam
E = 200*(10**9)
I= 0.001

    #These functions are the necessary formulas for the beamDeflection function.
def formula_both_1(W, l, E, I, a, x):
    return (W*(l-a)*x*(l**2-x**2-(l-a)*W*2))/(6*E*I*l)
def formula_both_2(W, l, E, I, a, x):
    return (W*a*(l-x)*(l**2-(l-x)**2-a**2))/(6*E*I*l)
def formula_cantilever_1(W, l, E, I, a, x):
    return W*x**2*(3*a-x)/(6*E*I)
def formula_cantilever_2(W, l, E, I, a, x):
    return W*a**2*(3*x-a)/(6*E*I)

def beamDeflection(positions, beamLength, loadPosition, loadForce,beamSupport):
    # beamDeflection(Calculates the deflection of the beam)
    #
    #Input      positions:(type: array of floats) All the different points along the beam where deflection
    #                     is being calculated for every elements of it.
    #           beamlength:(type: float)Length of the beam.(meter)
    #           loadPosition:(type: float) The position of the load from the very left point.(meter)
    #           load force:(type: float) The magnitude of the force.(kN)
    #           beamSupport:(type: integer)Numbers correlating to beam types
    #Output     deflection:(type: array of floats) Deflections correlating to every points of the positions
    #                       vector.
    
    
    
    #defining an array of zerros for deflections of positions
    deflection = np.zeros(len(positions))
    
    #computing deflection by applying formulas for support on both ends
    if beamSupport == 1:
        i=0
        for element in positions:
            if element < loadPosition:
                deflection[i]= formula_both_1(loadForce,beamLength,E,I,loadPosition,element)
            else:
                deflection[i]= formula_both_2(loadForce,beamLength,E,I,loadPosition,element)
            i=i+1
        return deflection
    #computing deflection by applying formulas for cantilever support type
    else:
        i=0
        for element in positions:
            if element < loadPosition:
                deflection[i] = formula_cantilever_1(loadForce, beamLength, E, I, loadPosition, element)
            else:
                deflection[i] = formula_cantilever_2(loadForce, beamLength, E, I, loadPosition, element)
            i = i + 1
    return deflection
