def beam_type_error(beam_type):
    if beam_type != 1 and beam_type != 2:
        print("Please type a valid beam type")


def beam_length_error(beam_length):
    if not isinstance(beam_length, float):
        print("This is not a valid decimal number or integer")

    if beam_length < 0:
        print("Please type a valid beam length because it seems like you typed negative number")


def choice1(beam_length, beam_type):
    while True:
        try:
            beam_length = float(input("Please enter the length of the beam\n>>"))
        except:
            print("This is not a valid number\n")
            continue
        if beam_length<0:
            print("Please type a valid beam length because it seems like you typed negative number\n")
            continue
        while True:
            try:
                beam_type = int(input("Please enter the beam support type\n>>"))
            except:
                print("This is not a valid option.\n>>")
                continue
            if beam_type != 2 and beam_type != 1:
                print("This is not a valid option")
                continue
            break

        break
    return beam_length, beam_type