import pandas as pd
import numpy as np
def load():
    filename=input("What is the name of the file?")
    df = pd.read_csv(filename, sep=',', header=None)
    beam_length=df[0][1]
    beam_type=df[0][0]
    array=np.array([],[])

    load_force=df.loc[0,:]
    load_position=df.loc[1,:]

    load_force=load_force.loc[1:][:]
    load_position=load_position.loc[1:][:]

    load_force = np.array([float(x) for x in load_force])
    load_position = np.array([float(x) for x in load_position])


    if beam_type!=1 or beam_type!=2:
        beam_type=1

        return load_force,load_position, beam_length, beam_type
