import matplotlib.pyplot as plt # Import the matplotlib.pyplot module
from beamDeflection import *
from beamSuperposition import *
def plot_type_oriented(beamLength, loadPositions, loadForces, beamSupport):
    #beamPlot(Plots the deflection-position graph)
    #Input      beamlength:(type: float)Length of the beam.(meter)
    #           loadPositions:(type: array of floats) The position of the loads from the very left point.
    #                       (meter)
    #           loadForces:(type: array of float) The magnitude of the loads.(kN)
    #           beamSupport:(type: integer)Numbers correlating to beam types.(1 for both end type,2 for 
    #                       cantilever)
    interval_from_the_user=float(input("Decide an interval for the points that you want to see."))
    #interval from the user is just an indicator of how frequent the points will be calculated.This 
    #is asked to the user. This could also be adjusted to a default number 0.001 but we preferred to ask
    # the user. 
    positions=np.arange(0, beamLength + interval_from_the_user, interval_from_the_user)

    props={}
    if beamSupport==1:
        deflections = np.array(-beamSuperposition(positions, beamLength,loadPositions, loadForces, beamSupport))
        plt.plot(positions, deflections, lw=5)
        #Placing the force data to the positions of the loads
        for counter,element in enumerate(loadPositions):
            if element!=0:
                bbox = {'fc': '1', 'pad': 0}
                props={'ha': 'center', 'va': 'center', 'bbox': bbox}
                text = str(loadForces[counter])+ " kN force at " + str(element)
                plt.text(element, 0, text, props, rotation=90)
                
        
        #maxdeflection is found and put on the graph
        max_deflection=0
        a = np.amax(deflections)
        b = np.amin(deflections)
        if a>-b:
            max_deflection=a
        else:
            max_deflection=b
        for position, deflection in zip(positions, deflections):
            if deflection==max_deflection:
                plt.text(0, deflection, "Max deflection point", props, rotation=0)
                plt.plot(position, deflection, '-gD')
        plt.title("Beam deflection")
        plt.xlabel("Points along the beam")  # Set the x-axis label
        plt.ylabel("Deflection")  # Set the y-axis label
        plt.xlim([0, beamLength])  # Set the limits of the x-axis
        plt.show()
    elif beamSupport==2:
        deflections = np.array(-beamSuperposition(positions, beamLength,loadPositions, loadForces, beamSupport))
        plt.plot(positions, deflections, lw=5)
        #Placing the force data to the positions of the loads
        for counter,element in enumerate(loadPositions):
            if element!=0:
                bbox = {'fc': '1', 'pad': 0}
                props={'ha': 'center', 'va': 'center', 'bbox': bbox}
                text = str(loadForces[counter])+ " kN force at " + str(element)
                plt.text(element, 0, text, props, rotation=90)
                
        
        #maxdeflection is found and put on the graph
        max_deflection=0
        a = np.amax(deflections)
        b = np.amin(deflections)
        if a>-b:
            max_deflection=a
        else:
            max_deflection=b
        for position, deflection in zip(positions, deflections):
            if deflection==max_deflection:
                plt.text(0, deflection, "Max deflection point", props, rotation=0)
                plt.plot(position, deflection, '-gD')
        plt.title("Beam deflection")

        plt.xlabel("Points along the beam")  # Set the x-axis label
        plt.ylabel("Deflection")  # Set the y-axis label

        plt.xlim([0, beamLength])  # Set the limits of the x-axis


        plt.show()