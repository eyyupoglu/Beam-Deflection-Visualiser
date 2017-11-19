import numpy as np

import math

E = 200*(10**9)
I= 0.001
beam_length= float(input("enter the beam length please"))
interval_from_the_user= float(input("enter interval"))

positions = np.arange(0,beam_length+interval_from_the_user,interval_from_the_user)


def formula_both_1(W, l, E, I, a, x):
    return (W*(l-a)*x*(l**2-x**2-(l-a)**2))/(6*E*I*l)
def formula_both_2(W, l, E, I, a, x):
    return (W*a*(l-x)*(l**2-(l-x)**2-a**2))/(6*E*I*l)
def formula_cantilever_1(W, l, E, I, a, x):
    return W*x**2*(3*a-x)/(6*E*I)
def formula_cantilever_2(W, l, E, I, a, x):
    return W*a**2*(3*x-a)/(6*E*I)

def beamDeflection(positions, beamLength, loadPosition, loadForce,beamSupport):

    deflection = np.zeros(len(positions))
    if beamSupport == 1:
        i=0
        for element in positions:
            if element < loadPosition:
                deflection[i]= formula_both_1(loadForce,beamLength,E,I,loadPosition,element)
            else:
                deflection[i]= formula_both_2(loadForce,beamLength,E,I,loadPosition,element)
            i=i+1
        return deflection
    else:
        i=0
        for element in positions:
            if element < loadPosition:
                deflection[i] = formula_cantilever_1(loadForce, beamLength, E, I, loadPosition, element)
            else:
                deflection[i] = formula_cantilever_2(loadForce, beamLength, E, I, loadPosition, element)
            i = i + 1
        return deflection

test_1 = beamDeflection(np.arange(0,11,1), 10, 1,  50, 1)
