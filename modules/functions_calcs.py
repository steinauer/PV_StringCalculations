#functions_calcs.py
#Module to contain calculation functions

#import math for inbuilt Python mathematics
import math

"=========================================================================================================="
#Calculation -> temperature adjustment, adjusts given parameter for temperature
#NOTE temperature STC inputted at 25deg. C
def temp_adjust(temp_coefficient, Parameter_STC, Temp_actual):
    temp_adjusted = Parameter_STC + (((temp_coefficient/100)*Parameter_STC) *(Temp_actual - 25))

    return temp_adjusted
"=========================================================================================================="    
#adjusts for cable drops
def cable_drop(value, drop_percentage):
    return ((1-(drop_percentage/100))*value)
"=========================================================================================================="
#adjusts according to safety factor
#NOTE: adjust to positive or negative depending on which calculation is chosen
def safetyfact_adjust(value, factor_percentage):
    return ((1+(factor_percentage/100))*value)
"=========================================================================================================="
#Calculation -> Minimum number of modules in string = min. MPPT voltage / min module voltage (at X deg. C, max temp)
def min_modules(MPPTvolt_min, Modulevolt_min):
    minimum_modules = MPPTvolt_min / Modulevolt_min

    
    print("Minimum number of modules per string is: ")
    #round up to nearest whole number
    if not math.isnan(minimum_modules):
        minimum_modules = math.ceil(minimum_modules)
    print(minimum_modules)
    return minimum_modules
"=========================================================================================================="

#Calculation -> maximum number of modules = max inverter voltage (safety margin adjusted) / max module voltage (at X deg. C, min temp)
#For Vmp and Vmmpt_max and for Voc and Inv_volt absolute max 
def max_modules(Invvolt_max, Modulevolt_max):
    maximum_modules = Invvolt_max/ Modulevolt_max

    
    #round down to nearest whole number
    if not math.isnan(maximum_modules):
        maximum_modules = math.floor(maximum_modules)
    
    print("Maximum number of modules per string is: ")
    print(maximum_modules)
    return maximum_modules
"=========================================================================================================="

#Calculation -> maximum number of strings
def max_strings(Invcurrent_max, Modulecurrent_max):
    maximum_strings = Invcurrent_max / Modulecurrent_max

    #round down to nearest whole number
    if not math.isnan(maximum_strings):
        maximum_strings = math.floor(maximum_strings)

    print("Maximum number of strings per inverter input is: ")
    print(maximum_strings)
    return maximum_strings
"=========================================================================================================="
#Calculation -> maximum number of modules in array, from power rating of inverter
def max_totalmodules(Invpower_ratedmaxPV, Modulepower):
    maximum_totalmodules = (Invpower_ratedmaxPV*1.2) / Modulepower

    #round down to nearest whole number
    if not math.isnan(maximum_totalmodules):
        maximum_totalmodules = math.floor(maximum_totalmodules)
    

    print("Maximum total number of modules per inverter:   ")
    print(maximum_totalmodules)

    
    return(maximum_totalmodules)
"=========================================================================================================="



#Calculation -> Array calculator, from min to max modules in string, and max no. strings taken into account, and total number panels
#IDEAS: Give a buffer of +- 10 or so panels to total panel number, then calculate possible arrays from that, then maybe consider subtracting from one or two strings to get total number of panels accurate

#Test for using user input as keyword argument in function (for user to choose between Voc max_modules or Vmp max_modules)
def test_call(**options):
    if options.get("Test")== "A":
        print("Option A")
    elif options.get("Test")=="B":
        print("Option B")
    else:
        print("No option chosen")


def array_config(min_modules, voc_maxmodules, vmp_maxmodules, max_strings, no_modules, **options):
    pass
