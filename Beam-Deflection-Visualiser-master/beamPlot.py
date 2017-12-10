import matplotlib.pyplot as plt # Import the matplotlib.pyplot module
import matplotlib.patches as mpatches
from beamDeflection import *
from beamSuperposition import *
def beamPlot(beamLength, loadPositions, loadForces, beamSupport):
    #beamPlot(Plots the deflection-position graph)
    #Input      beamlength:(type: float)Length of the beam.(meter)
    #           loadPositions:(type: array of floats) The position of the loads from the very left point.
    #                       (meter)
    #           loadForces:(type: array of float) The magnitude of the loads.(kN)
    #           beamSupport:(type: integer)Numbers correlating to beam types.(1 for both end type,2 for 
    #                       cantilever)
#---------------------------------------------------------------------------------------------------------------------------
    #interval from the user is just an indicator of how frequent the points will be calculated.This 
    #is asked to the user. This could also be adjusted to a default number 0.001 but we preferred to ask
    # the user. 
    
    interval_from_the_user=0.1
    while True:
        interval_from_the_user=input("-You need to decide an interval for the points that you want to calculate\n\n-You can type 0.1 if you want to calculate every 0.1 m on the beam.\n\nQ . Quit to main menu\n\n>> ")
        if interval_from_the_user=="q" or interval_from_the_user=="Q":
            return 0
        try:
            interval_from_the_user=float(interval_from_the_user)
        except:
            print("Not a valid input. Please type a character which can be converted into float")
            continue
        if interval_from_the_user <=0: 
            print("You have typed either a negative value or zero. Please type a valid positive integer/float or type \"Q\" to escape ")
            continue
        break
##################################################################################################################################
   
    #Now we will construct a positions array ranging from 0 to beam length. So that we will compute deflections at those points
    positions=np.arange(0, beamLength + interval_from_the_user, interval_from_the_user)
    props={}
    plt.grid(True)
    #NOTe THAT beamSuperposition() has a negative sign because we thought it would be more realistic if the graph is downward as 
    #we see in the sketch in project criteria file.
    deflections = np.array(-beamSuperposition(positions, beamLength,loadPositions, loadForces, beamSupport))
    plt.plot(positions, deflections, lw=5)
    #Placing the force data to the positions of the loads
    for counter,element in enumerate(loadPositions):
        if element!=0:
            bbox = {'fc': '1', 'pad': 0}
            props={'ha': 'center', 'va': 'top', 'bbox': bbox}
            text = str(loadForces[counter])+ " kN force at " + str(element) + " meter"
            plt.text(element, 0, text, props, rotation=90, color = "red")
##################################################################################################################################
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
            if len(deflections[deflections!=0])==0:#if all the deflection values are zero.
                green_patch = mpatches.Patch(color='green', label='There is no one maximum deflection')
                plt.legend(handles=[green_patch])
                break#we should break the for loop because we dont want to put green point to every zero value because all of them are the same and zeros
            plt.text(0, deflection, "Max deflection point", props, rotation=0, color="green")
            plt.plot(position, deflection, '-gD')
##################################################################################################################################
    #Labels and titles are set
    plt.title("BEAM DEFLECTION PLOT")
    plt.xlabel("Points along the beam")  # Set the x-axis label
    plt.ylabel("Deflection")  # Set the y-axis label
    plt.xlim([0, beamLength])  # Set the limits of the x-
    if beamSupport==1: 
        label = 'There is no one maximum deflection\nBeam type: Both end type\nBeam length: '+str(beamLength)+"m"
    else:
        label = 'There is no one maximum deflection\nBeam type: Cantilever type\nBeam length: '+str(beamLength)+"m"
    if len(deflections[deflections!=0])==0:#if all the deflection values are zero.
        green_patch = mpatches.Patch(color='green', label=label)
        plt.legend(handles=[green_patch])
    else:
        if beamSupport==1: 
            label = 'Max deflection point \nBeam type: Both end type\nBeam length: '+str(beamLength)+"m"
        else:
            label = 'Max deflection point \nBeam type: Cantilever type\nBeam length'+str(beamLength)+"m"
        green_patch = mpatches.Patch(color='green', label=label)#max deflection legend 
        plt.legend(handles=[green_patch])#giving a green color
    plt.show()#showing the object
