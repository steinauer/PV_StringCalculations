#main.py
#Main file for Calculation_Automation_Python Project


#import math for inbuilt Python maths capabilities
import math
#import pandas for creating DataFrame
import numpy as np
import pandas as pd
#import csv for writing to csv file
import csv

#import functions from functions_module_calcs and functions_module_other

from modules import functions_other
from modules import functions_calcs

#create dataframe based on csv file with list of parameters called "List_of_parameters.csv"
dataframe = pd.read_csv('List_of_parameters.csv')
print(dataframe)
print("--------------------------------------------------------------")
print()


#test
#dataframe.iat[1,0] = functions_other.user_input("Vmppt_min", "Volts")
#dataframe.iat[0,0] = functions_other.user_input("Vmp", "Volts")

#print dataframe to see values have been entered
#print(dataframe)
#print("--------------------------------------------------------------")
#print()

"=========================================================================================================================="
#CALCULATIONS for minimum modules/string

#adjust Vmp for maximum temperature
#also checks for temperature coeff, if no value for Vmp_coeff, passes Pmp_coeff, if no value for either, passes Voc_coeff
if math.isnan(dataframe.iat[5,0]):
    if math.isnan(dataframe.iat[15,0]):
        #no value for either, passes Voc_coeff
        temporary = functions_calcs.temp_adjust(dataframe.iat[6,0],dataframe.iat[0,0],dataframe.iat[17,0])
    else:
        #no value for Vmp_coeff, passes Pmp_coeff
        temporary = functions_calcs.temp_adjust(dataframe.iat[15,0],dataframe.iat[0,0],dataframe.iat[17,0])        
else:
    temporary = functions_calcs.temp_adjust(dataframe.iat[5,0],dataframe.iat[0,0],dataframe.iat[17,0])
#save Vmp_min_tempadjusted
Vmp_min_tempadjusted = temporary
#adjust again for cable drop
if math.isnan(dataframe.iat[9,0]):
    temporary = functions_calcs.cable_drop(temporary, 0)
else:
    temporary = functions_calcs.cable_drop(temporary, dataframe.iat[9,0])
#adjust Inverter Vmmpt_min for safety factor
if math.isnan(dataframe.iat[7,0]):
    #checks if safety factor has no value given, passes 0 if empty
    temporary2 = functions_calcs.safetyfact_adjust(dataframe.iat[1,0], 0)
else:
    temporary2 = functions_calcs.safetyfact_adjust(dataframe.iat[1,0], dataframe.iat[7,0])
#calling min modules function inputting adjusted values
min_modules = functions_calcs.min_modules(temporary2, temporary)

"=========================================================================================================================="
#CALCULATIONS for maximum modules/string from Voc, Vinv_max

#adjust Voc for minimum temperature
temporary = functions_calcs.temp_adjust(dataframe.iat[6,0], dataframe.iat[3,0],dataframe.iat[16,0])
#saves Voc_max_tempadjusted
Voc_max_tempadjusted = temporary
#adjust Inverter_volt Max input for safety factor
if math.isnan(dataframe.iat[8,0]):
    #checks if safety factor has no value given, passes value of 0
    temporary2 = functions_calcs.safetyfact_adjust(dataframe.iat[4,0], 0)
else:
    temporary2 = functions_calcs.safetyfact_adjust(dataframe.iat[4,0],dataframe.iat[8,0])
#calling max module function inputting adjusted values
max_modules_Voc = functions_calcs.max_modules(temporary2, temporary)

#CALCULATIONS for minimum Voc temp adjusted
Voc_min_tempadjusted = functions_calcs.temp_adjust(dataframe.iat[6,0], dataframe.iat[3,0],dataframe.iat[17,0])

"=========================================================================================================================="
#CALCULATIONS for maximum modules/string from Vmp, Vmmpt_max

#adjust Vmp for minimum temperature
#checks for temp coefficients, if no value for Vmp_coeff, passes Pmp_coeff, if no value for either, passes 0
if math.isnan(dataframe.iat[5,0]):
    if math.isnan(dataframe.iat[15,0]):
        #no value for either, passes Voc_coeff
        temporary = functions_calcs.temp_adjust(dataframe.iat[6,0],dataframe.iat[0,0],dataframe.iat[16,0])
    else:
        #no value for Vmp_coeff, passes Pmp_coeff
        temporary = functions_calcs.temp_adjust(dataframe.iat[15,0],dataframe.iat[0,0],dataframe.iat[16,0])
else:
    temporary = functions_calcs.temp_adjust(dataframe.iat[5,0],dataframe.iat[0,0],dataframe.iat[16,0])
#adjust Inverter Vmmpt_max for safety factor
if math.isnan(dataframe.iat[8,0]):
    #checks if safety factor value is empty, passes 0 if so
    temporary2 = functions_calcs.safetyfact_adjust(dataframe.iat[2,0], 0)
else:
    temporary2 = functions_calcs.safetyfact_adjust(dataframe.iat[2,0], dataframe.iat[8,0])
#calling max module function inputting adjusted values
max_modules_Vmp = functions_calcs.max_modules(temporary2, temporary)

"=========================================================================================================================="
#CALCULATIONS for maximum number of strings

#adjust Isc (max module current) to temperature
#since Current does not vary much with temperature change, Isc is used as the maximum module current
#calling max strings function
max_strings_perinput = functions_calcs.max_strings(dataframe.iat[10,0],dataframe.iat[11,0])
max_strings = max_strings_perinput * dataframe.iat[18,0]
print("Maximum number of strings per inverter is: %d" %(max_strings))
#multiply by number of inverters 
max_stringsfinal = max_strings * dataframe.iat[20,0]
print('Maximum number of strings for entire array is: %d' %max_stringsfinal)

#CALCULATIONS for maximum number of modules per inverter with 20% oversizing
max_totalmodules = functions_calcs.max_totalmodules(dataframe.iat[13,0],dataframe.iat[14,0])
"=========================================================================================================================="

Voc_totalmax = max_modules_Voc * dataframe.iat[3,0]
Isc_max_array = max_strings * dataframe.iat[11,0]

"=========================================================================================================================="

results_header = ['Description', 'Value']
results = [['min_modulesperstring',min_modules],
           ['max_modulesperstring_Voc',max_modules_Voc],
           ['max_modulesperstring_Vmp',max_modules_Vmp],
           ['max_strings_perinput',max_strings_perinput],
           ['max_strings_perinverter',max_strings],
           ['max_strings_total',max_stringsfinal],
           ['max_totalmodules', max_totalmodules]]

extra_results = [['Maximum Voc temperature adjusted', Voc_max_tempadjusted],
                 ['Minimum Voc temperature adjusted', Voc_min_tempadjusted],
                 ['Minimum Vmp temperature adjusted', Vmp_min_tempadjusted]]

#create a csv file with results
with open ('Results.csv', 'w', encoding = 'UTF8', newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(results_header)
    writer.writerows(results)
    writer.writerow([])
    writer.writerow(['Maximum Voc based on max modules in string', Voc_totalmax])
    writer.writerow(['Maximum Isc', Isc_max_array])
    writer.writerow([])
    writer.writerows(extra_results)

dataframe_answers = pd.read_csv('Results.csv')

print(dataframe_answers)


'========================================================================================================='

#messing around with answers to get array config
#simply dividing total modules by range from min modules to max modules
inverter_rating_total = dataframe.iat[13,0] * dataframe.iat[20,0]
panel_rating = dataframe.iat[14,0]
total_modules = dataframe.iat[19,0]
for modules in range(min_modules, max_modules_Voc +1):
    temp1 = math.floor(total_modules/modules)
    temp2 = math.ceil(total_modules/modules)

#cleaning up code with Boolean
    x1 = bool(temp1<=max_stringsfinal)
    y1 = bool(((modules*temp1)*panel_rating)<= (inverter_rating_total*1.2))
    z1 = bool((modules*temp1)==total_modules)
    x2 = bool(temp2<=max_stringsfinal)
    y2 = bool(((modules*temp2)*panel_rating)<= (inverter_rating_total*1.2))
    z2 = bool((modules*temp2)==total_modules)
#only outputs answer if within max string range, and also within 20% oversizing, for exact number of modules 
    if x1 and y1 and z1:
        print("Config: %d x %d, total modules: %d"%(modules,temp1,modules*temp1))
        if total_modules<(modules*temp1):
            print("Extra modules needed: %d" %((modules*temp1)-total_modules))
        else:
            print("Modules leftover: %d" %(total_modules-(modules*temp1)))
    if x2 and y2 and z2:
        print("Config: %d x %d, total modules: %d"%(modules,temp2,modules*temp2))
        if total_modules<(modules*temp2):
            print("Extra modules needed: %d" %((modules*temp2)-total_modules))
        else:
            print("Modules leftover: %d" %(total_modules-(modules*temp2)))
    
#to print the remaining array configs with extra or fewer modules required as well, simply remove z1 or z2


#user input should exit exe program
exitcommand = input('Press Enter key to exit')
print("exiting...")
