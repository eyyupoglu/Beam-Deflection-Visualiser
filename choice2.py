from display_menu import *

def display_forces(load_positions,load_forces):
    k = 0
    if np.any(load_positions):
        for element in load_positions:
            if element != 0:
                print(load_forces[k], "kN force is on ", element, "meter away from the very left point.")
            k = k + 1
def choice2(load_positions, load_forces, conf_load_menu, i):
    display_forces(load_positions, load_forces)
    choice= display_menu(conf_load_menu)
    if choice == 1:
        load_forces[i] = float(input("The magnitude of the load?"))
        load_positions[i] = float(input("The location of the load?"))
        i = i + 1
    elif choice == 2:
        load_positions = np.zeros(20)
        load_forces = np.zeros(20)
        print("Now you do not have any loads.")
    elif choice ==3:
        print("Which one do you want to remove? These are the positions from left point.")
        for counter,element in enumerate(load_forces):
            if element!=0:
                print(counter, " for", element,"position")
        try:
            jk=int(input(">>"))
            load_forces[jk]=0
            load_positions[jk]=0
        except:
            print("Error2")


    return load_positions, load_forces, i