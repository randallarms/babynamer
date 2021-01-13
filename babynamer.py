#======================================#
#              BabyNamer               #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

from random import randint
import os

# Opening text
print("\n\n=========")
print("BABYNAMER")
print("=========")
print("Generate a baby name based on popular baby names!")

# Acceptable values
years = ["2018, 2019"]
genders = ["female", "f", "male", "m", "girl", "girls", "boy", "boys"]
booleans = ["yes", "y", "no", "n", "true", "false"]

# Name generation
def name_gen(year, gender, middle_option):

    # Check year selction
    if not year in years:
        print("\nYear not found! ")
        exit()

    # Determine gender
    if not gender in genders:
        print("\nGender not found! ")
        exit()
    elif gender.lower() == "m" or gender.lower() == "male" or gender.lower() == "boy" or gender.lower() == "boys":
        gender = "male"
    else:
        gender = "female"
        
    # Determine if generating middle name
    if not middle_option in booleans:
        print("\nMiddle name setting not recognize! ")
        exit()
    elif middle_option.lower() == "y" or middle_option.lower() == "yes" or middle_option.lower() == "true":
        middle_option = True;
    else:
        middle_option = False;
    
    # Get files
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
    f_names = open(os.path.join(__location__, "names/" + year + "/" + gender + ".txt"), "r")
    
    # Fill list of possible names from file
    names = []
    for line in f_names:
        names.append(line)

    # Generate name
    name_str = ""
    name_str += names[randint(0, len(names)-1)].strip('\n')
    if middle_option == True:
        name_str += " " + names[randint(0, len(names)-1)].strip('\n')
    return name_str
        
    file.close()

# Get the year
print("\nWhich year do you wish to draw popular baby names from? (Options: 2018-2019)")
y = input("> ");

# Get the gender
print("\nWhich gender do you wish to draw popular baby names from? (Options: boy, girl)")
g = input("> ");

# Get the middle name option
print("\nDo you want middle name suggestions, too? (Options: yes, no)")
m = input("> ");

# Generate the name
name = name_gen(y, g, m)

# Print the results
print("\nBaby name: ")
print(name + "\n")

# Go again prompt
again = True
    
while again == True:
    print("\nWant to generate a name with the same parameters? (Options: yes, no)")
    a = input("> ");

    if not a.lower() in booleans or a.lower() == "n" or a.lower() == "no" or a.lower() == "false":
        print("\nGoing back to menu... ")
        again = False;
    if a.lower() == "y" or a.lower() == "yes" or a.lower() == "true":
        again = True;
        name = name_gen(y, g, m)
        print("\nBaby name: ")
        print(name + "\n")
    