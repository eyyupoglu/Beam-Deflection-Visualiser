from display_menu import *
from helpingFunctions import *
conf_load_menu=np.array(["Add load",
                         "Remove all loads",
                         "Remove one load",
                         "Quit to main menu"])
def display_forces(load_positions,load_forces):
    k = 0
    if np.any(load_positions):
        for element in load_positions:
            if element != 0:
                print(load_forces[k], "kN force is on ", element, "meter away from the very left point.")
            k = k + 1
    if len(load_forces[load_forces!=0])==0:
        print("There is no force acting on the beam\n")
        return
def choice2(load_positions, load_forces, conf_load_menu, i, beam_length):
    while True:
        clear_screen()
        print("*************************************CONFIGURE LOADS*******************************************")
        display_forces(load_positions, load_forces)
        choice= display_menu(conf_load_menu)
        esc=0
        if choice == 1:
            while (esc!="q" and esc!="Q"):
                print("Q . Quit\n")
                esc=input("The magnitude of the load?\n>>")
                try:
                    load_forces[i] = float(esc)
                except:
                    load_forces[i]=0
                    print("This is not a valid input.(Type in a number!)\n")
                    continue
                if load_forces[i]<0:
                    print("Please type in a positive value!\nor")
                    load_forces[i]=0
                    continue
                while True:
                    print("Q . Quit\n")
                    esc=input("Location of the load?\n>>")
                    if esc=="q" or esc=="Q":
                        load_forces[i]=0
                        break#ESCAPE BUTTON
                    try:
                        load_positions[i] = float(esc)
                    except:
                        load_positions[i]=0
                        
                        print("This is not a valid number. Please type a number!")
                        continue
                    if load_positions[i] < 0 or load_positions[i]> beam_length:
                        print("Please type a number between 0 and length of the beam(",beam_length," m)")
                        load_positions[i]=0
                        continue
                    break
                break
                
                
            #i is for keeping track of places of new forces and positions
            i = i + 1
        elif choice == 2:
            load_positions = np.zeros(100)
            load_forces = np.zeros(100)
            i=0
            print("Now you do not have any loads.")
        elif choice ==3:
            if len(load_forces[load_forces!=0])==0:
                print("There is no force to be removed\n")
                continue
            button="mike"
            print("Which one do you want to remove? These are the positions from left point.\n")
            while True:
                for counter,element in enumerate(load_forces):
                    if element!=0:
                        print(counter+1, " for the force at ", load_positions[counter],"meter position")
                print("Q Quit to main menu")
                button=input(">>")
                if button=="q" or button=="Q":
                    break
                try:
                    load_forces[int(button)-1]=0
                    load_positions[int(button)-1]=0
                except:
                    print("This value either not an integer or an illegal input ")
                    continue
        elif choice==4:
            return load_positions, load_forces, i
        else:
            print("Please type a valid input.\n")


    