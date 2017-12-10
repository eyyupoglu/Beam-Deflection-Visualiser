#--------------------------Initialization--------------------------------------------
import pandas as pd
import numpy as np
import os
from display_menu import *

#defining menu options to display
save_menu_options= np.array(["Change Directory",
                            "Stay in the current directory",
							"Display the files in current directory",
                             "Quit"])


def load(load_forces,load_positions,beam_length,beam_type):
    #the load function loads a file into the program. It splits the matrix of a saved file up and assign the certain values to 
    #load_forces,load_positions,beam_length and beam_type.
    #Input: User input
	path=os.getcwd()
	while True:
		#displaying directory
        print("Now you are in this directory; \n  ",os.getcwd(),"\n")
		#displaying menu
        button=display_menu(save_menu_options)
		if button==1:
        #redefining path
			path=input("Type the file location you want to load the file from\n>>")
		elif button==2:
        #staying with this directory
			path=os.getcwd()
		elif button==3:
        #printing content of current directory
			print(os.listdir(path) )
			continue
		elif button==4:
		#While loop is broken with QUIT option
			break
		while True:
			try:
				print("Q . Quit")
				filename=input("What is the name of the file?\n>>")
				if filename=="Q"or filename=="q":break #implementing quit option to go one submenu back
				
            #reading the file in and storing in variable df    
            df = pd.read_csv(path+"/"+filename, header=None)
				
            #assigning values
            beam_length=df[0][1]
				beam_type=df[0][0]	
				load_forces=df.loc[0,:]
				load_positions=df.loc[1,:]
				load_forces=load_forces.loc[1:][:]
				load_positions=load_positions.loc[1:][:]
				load_forces = np.array([float(x) for x in load_forces])
				load_positions = np.array([float(x) for x in load_positions])
				
            #if for some reason the beam support type is not equal 1 or 2 we set it to both ends by default
            if beam_type!=1 or beam_type!=2:
					beam_type=1
                    
        #error message
			except:
				print(filename+" file is not found please make sure the followings;\n* Make sure you are in the correct directory\n"+
				"* Make sure you type the correct extension(.csv)\n")
				continue
			break
		break
    #return values
	return load_forces,load_positions, beam_length, beam_type
