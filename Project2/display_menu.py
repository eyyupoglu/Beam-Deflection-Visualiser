import numpy as np


def input_number(prompt):
    try:
        choice=float(input(prompt))


    except ValueError:
        print("Type in a valid number!\n>>")
        return 0
    return choice

def display_menu(options):
    i=0
    for element in options:

        print(i+1,".",element,"\n")
        i=i+1

    choice=0

    while not(np.any(choice==np.arange(len(options))+1)):
       choice=input_number("Choose an option\n>>")
       if not (np.any(choice==np.arange(len(options))+1)):
            print("Please choose one of the options\n>>")



    return choice


