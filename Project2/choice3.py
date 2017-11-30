import os,numpy as np
from main import *

save_menu_options= np.array(["Change Directory",
                            "Stay in the current directory",
                             "Quit"])
#This function is to merge load positions and load_forces together so that we will store them together. Every point will
#correlate with the force that it has on it.
def merge(load_positions, load_forces, beam_type, beam_length):
    exactly=np.array([beam_length,beam_type])
    exactly=np.vstack(exactly)
    long_array=np.vstack((load_forces,load_positions))
    exactly=np.hstack((exactly,long_array))
    return exactly

def save(beam_length, beam_type, load_positions, load_forces):

    print("Now you are in this directory \n ",os.getcwd())
    button=display_menu(save_menu_options)
    if button==1:
        path=input("Type the file location you want to save the file to\n>>")
    elif button==2:
        path=os.getcwd()
    elif button==3:
        return 0
    os.chdir(path)
    filename = input("Type a file name\n>>")

    np.savetxt(filename+".csv", merge(load_positions,load_forces, beam_length, beam_type), delimiter=',')
    return 0

