#functions_module_other
#file to contain user input, printing, verification, menu functions



#Function to obtain user input, verifies that what has been entered is an accepted number
#NOTE: may also need to verify that only positive numbers are accepted 

def user_input(parameter, units):
    while True:
        print()
        value = input("Enter %s in %s:     " %(parameter, units))
        print()

        try:
            #convert to an integer and check if valid
            value = int(value)
            print("value %d is accepted"%value)
            print("------------------------------------------------------------")
            break;

        except ValueError:
            try:
            #convert it to a float and check if valid
                value = float(value)
                print("value %.5f is accepted"%value)
                print("------------------------------------------------------------")
                break;
            except ValueError:
                print("Value entered %s has not been accepted, try again"%value)
    return value    


#menu function
#NOTE to be edited to allow for selection of calculation, perhaps some sub-menus to enter values, read values
def main_menu():
    while True:

        print()
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("CHOOSE ONE OF THE FUNCTIONS BELOW BY SELECTING 1,2, or 3")
        print("------------------1. Adding Function--------------------------")
        print("------------------2. Multiplying Function---------------------")
        print("------------------3. Power Function---------------------------")
        print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print()

        value = input()

        try:
            #convert value to integer to check if valid
            value = int(value)
            if (value == 1) or (value == 2) or (value == 3):
                print("Value %d has been accepted" %value)
                break;
            else:
                print("Value entered %d has not been accepted. Enter a value 1, 2 or 3"%value)
                continue;
        except ValueError:
            print("Value entered %s has not been accepted, ENTER 1,2, or 3 and try again" %value)
    
    
    return value
