# ------------------------------------------------- #
# Title: Assignment 07
# Description: Pickling and Exception Handling Demo
# ChangeLog (Who,When,What):
# SDH,12.01.2020,Created script with demonstration of Pickling
#                and Exception Handling.
#                Based on answers from Assignments 03 and 05
# ------------------------------------------------- #

# Data -------------------------------------------- #

import pickle  # This imports code from another code file!

strFileName = "HomeInventory.dat"  # The name of the data file

# Processing -------------------------------------- #

def read_binary_file(file_name):
    obj_file = open(file_name, "rb")
    lst_of_data = pickle.load(obj_file)
    obj_file.close()
    return lst_of_data

def save_binary_file(file_name, str_list):
    obj_file = open(file_name, "wb")
    pickle.dump(str_list,obj_file)
    obj_file.close()

# Presentation ------------------------------------ #

# Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Display contents of file
    2) Replace contents of file
    3) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 3] - "))
    print()  # adding a new line for looks

    # Show the current item in the binary file
    if (strChoice.strip() == '1'):
        print(read_binary_file(strFileName))
        continue

    # Enter a new item and write it to the binary file
    elif (strChoice.strip() == '2'):
        str_item = input("Enter an Item Name: ")

        try:
            flt_value = float(input("Enter an Estimated Value: $"))
            str_list = str_item + ", " + str(flt_value)
            print(str_list)
            save_binary_file(strFileName, str_list)

        except:
            print("Please enter a number!")
            flt_value = float(input("Enter an Estimated Value: $"))
            str_list = str_item + ", " + str(flt_value)
            print(str_list)
            save_binary_file(strFileName, str_list)

        continue

    # Exit program
    elif (strChoice.strip() == '3'):
        break  # Exit the program