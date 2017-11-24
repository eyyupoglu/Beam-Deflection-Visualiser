import os,numpy as np

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
    path=input("Type the file location you want to save the file to\n>>")
    os.chdir(path)
    filename = input("Type a file name\n>>")

    np.savetxt(filename+".csv", merge(load_positions,load_forces, beam_length, beam_type), delimiter=',')

