import matplotlib.pyplot as plt # Import the matplotlib.pyplot module

from beamDeflection import *

from beamSuperposition import *


def beamPlot(beamLength, loadPositions, loadForces, beamSupport):

    plt.plot(positions, -beamSuperposition(positions, beamLength,loadPositions, loadForces, beamSupport))
    plt.title("Simple line graph")

    plt.xlabel("x-values")  # Set the x-axis label
    plt.ylabel("y-values")  # Set the y-axis label

    plt.xlim([0, beam_length])  # Set the limits of the x-axis


    plt.show()

beamPlot(beam_length, np.array([50*beam_length/100]), np.array([1000]), 2)