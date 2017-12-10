#--------------------------Initialization--------------------------------------------
import os,numpy as np
from display_menu import *

#defining menu options to display
save_menu_options= np.array(["Change Directory",
                            "Stay in the current directory",
                             "Quit"])


def merge(load_positions, load_forces, beam_type, beam_length):
    #The merge function stores load positions and load_forces together in a matrix. Every point will
    #correlate with the force that it has on it.
    #Input: load postions, forces (array), beamtype(integer),beamlength (float)
    #Output: -  exactly, a 2xm matrix 
    
    #putting the current beamlenght and beamtype as first column in a matrix
    exactly=np.array([beam_length,beam_type])
    exactly=np.vstack(exactly)
    
    #connecting values of forces and postions to that matrix
    long_array=np.vstack((load_forces,load_positions))
    exactly=np.hstack((exactly,long_array))
    return exactly

def save_file(beam_length, beam_type, load_positions, load_forces):
    #save file saves the resulting matrix (see merge function) in a file.
    #Input:load postions, forces (array), beamtype(integer),beamlength (float)
    #Output: - saves the matrix to a file
    print("**************************************SAVE FILE******************************************")
    while True:
        print("Where do you want to save this very file?\n")
        print("Now you are in this directory; \n  ",os.getcwd(),"\n")
        
        #displaying menu
        button=display_menu(save_menu_options)
        
        #defining options
        if button==1:
            #changing file location
            path=input("Type the file location you want to save the file to\n>>")
        elif button==2:
            #staying in current one
            path=os.getcwd()
        elif button==3:
            #quit
            break
        try:
            #saving file
            os.chdir(path)
            filename = input("Type a file name\n>>")
            np.savetxt(filename+".csv", merge(load_positions,load_forces, beam_length, beam_type), delimiter=',')
        except:
            print("This very particular location is not found. Please type a valid directory.\n")
            continue
        break
    
