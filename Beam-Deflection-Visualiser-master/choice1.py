'''Function Regarding Choice 1 in main script'''

#--------------------------------------------Initialization--------------------------------------------------------------------
import numpy as np
from display_menu import *


#Defining an array for options displayed
choice1_options=np.array(["For both end support type beam",
                         "For cantilever type beam",
                         "Quit",
                         ])


def choice1(beam_length, beam_type):
#choice1 function displayes options regarding the beam and enables the  user to configure the beamlength and the beam support type.
#Input: user input
#Output: beamlength and support type (float & Integer, respectively)

    print("*************************************CONFIGURE BEAM*******************************************")
    while True:
        
        try:
            #checking beamlength is of float type
            beam_length = float(input("Please enter the length of the beam\n>>"))
            
        except:
            print("Unfortunately this is not a valid number\n")
            continue
        #checking if beamlength input is negative and giving feedback
        if beam_length<0:
            print("Please type a valid beam length because it seems like you typed in a negative number\n")
            continue
        #displaying options for beam support type
        while True:
            print("Please choose the beam support type\n")
            
            button = display_menu(choice1_options)
            
            if button==3 : break #ESCAPE option 
           
            #checking the input is an integer and equal to 1 and 2
            try: 
                beam_type=int(button)
            except:
                print("This is not a valid option.\n>>")
                continue
            if beam_type != 2 and beam_type != 1:
                print("This is not a valid option")
                continue
            break

        break
    return beam_length, beam_type