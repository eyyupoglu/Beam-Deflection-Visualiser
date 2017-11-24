import matplotlib.pyplot as plt # Import the matplotlib.pyplot module

from beamDeflection import *

from beamSuperposition import *


def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    interval_from_the_user=float(input("Decide an interval for the points that you want to see."))
    positions=np.arange(0, beamLength + interval_from_the_user, interval_from_the_user)
    if beamSupport==1:
        plt.plot(positions, -beamSuperposition(positions, beamLength,loadPositions, loadForces, beamSupport))
    elif beamSupport==2:
        plt.plot(positions, -beamSuperposition(positions, beamLength,loadPositions, loadForces, beamSupport))
    plt.title("Simple line graph")

    plt.xlabel("x-values")  # Set the x-axis label
    plt.ylabel("y-values")  # Set the y-axis label

    plt.xlim([0, beamLength])  # Set the limits of the x-axis


    plt.show()

"""beam_length=float(input("Beam length"))

beamPlot(beam_length, np.array([50*beam_length/100]), np.array([1000]), 2)"""