import pandas as pd
import numpy as np
import os
from display_menu import *
save_menu_options= np.array(["Change Directory",
                            "Stay in the current directory",
							"Display the files in current directory",
                             "Quit"])
def load(load_forces,load_positions,beam_length,beam_type):
	path=os.getcwd()
	while True:
		print("Now you are in this directory; \n  ",os.getcwd(),"\n")
		button=display_menu(save_menu_options)
		if button==1:
			path=input("Type the file location you want to load the file from\n>>")
		elif button==2:
			path=os.getcwd()
		elif button==3:
			print(os.listdir(path) )
			continue
		elif button==4:
			break
		while True:
			try:
				print("Q . Quit")
				filename=input("What is the name of the file?\n>>")
				if filename=="Q"or filename=="q":break
				df = pd.read_csv(path+"/"+filename, header=None)
				beam_length=df[0][1]
				beam_type=df[0][0]	
				load_forces=df.loc[0,:]
				load_positions=df.loc[1,:]
				load_forces=load_forces.loc[1:][:]
				load_positions=load_positions.loc[1:][:]
				load_forces = np.array([float(x) for x in load_forces])
				load_positions = np.array([float(x) for x in load_positions])
				if beam_type!=1 or beam_type!=2:
					beam_type=1
			except:
				print(filename+" file is not found please make sure the followings;\n* Make sure you are in the correct directory\n"+
				"* Make sure you type the correct extension(.csv)\n")
				continue
			break
		break
	return load_forces,load_positions, beam_length, beam_type
