#======================================#
#              BabyNamer               #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

from random import randint
import os

# Greeting text
print("\n\n=========")
print("BABYNAMER")
print("=========")
print("Open source @ github.com/randallarms/babynamer")

# Get file location
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
names_location = os.path.join(__location__, "names/")

# Acceptable values
genders = ["female", "f", "male", "m", "girl", "girls", "boy", "boys"]
booleans = ["yes", "y", "no", "n", "true", "false"] # Multipurpose for all y/n queries

# Get acceptable years by directory names with male & female names files
years = [] 
contents = os.listdir(names_location)

for item in contents:
    male_names_location = os.path.join(names_location, item + "/male.txt")
    female_names_location = os.path.join(names_location, item + "/female.txt")
    
    if os.path.isfile(male_names_location) and os.path.isfile(female_names_location):
        years.append(item)

# Name generation
def name_gen(year, gender, middle_option):

    # Check year selction
    if not year in years:
        print("\nError: Year not found! ")
        return False

    # Determine gender
    if not gender in genders:
        print("\nError: Gender not found! ")
        return False
    elif gender.lower() == "m" or gender.lower() == "male" or gender.lower() == "boy" or gender.lower() == "boys":
        gender = "male"
    else:
        gender = "female"
        
    # Determine if generating middle name
    if not middle_option in booleans:
        print("\nError: Middle name setting not recognized! ")
        return False
    elif middle_option.lower() == "y" or middle_option.lower() == "yes" or middle_option.lower() == "true":
        middle_option = True
    else:
        middle_option = False
    
    f_names = open(os.path.join(__location__, "names/" + year + "/" + gender + ".txt"), "r")
    
    # Fill list of possible names from file
    names = []
    for line in f_names:
        names.append(line)
        
    f_names.close()

    # Generate name
    name_str = ""
    name_str += names[randint(0, len(names)-1)].strip('\n')
    if middle_option == True:
        name_str += " " + names[randint(0, len(names)-1)].strip('\n')
    return name_str

# Menu, prompts
def menu():
    # Get the year
    print("\nWhich year do you wish to draw popular baby names from? (" + years[0] + "-" + years[len(years)-1] + ")")
    y = input("> ")

    # Get the gender
    print("\nWhich gender do you wish to draw popular baby names from? (boy/girl)")
    g = input("> ")

    # Get the middle name option
    print("\nDo you want middle name suggestions, too? (y/n)")
    m = input("> ")

    # Generate the name
    name = name_gen(y, g, m)
    
    # Unknown option selection warning
    if name == False:
        print("\nThere was an error generating names using the prompts specified. ")
        print("\nAvailable options can be found in the README file and on GitHub. ")
        return True
        
    else:
        # Print the results
        print("\nYour baby name: ")
        print(name + "\n")

        # Go again prompt
        again = True
            
        while again == True:
            print("\nWant to generate a name with the same parameters? (y/n)")
            a = input("> ");

            if not a.lower() in booleans or a.lower() == "n" or a.lower() == "no" or a.lower() == "false":
                again = False
                return True
            if a.lower() == "y" or a.lower() == "yes" or a.lower() == "true":
                again = True
                name = name_gen(y, g, m)
                print("\nBaby name: ")
                print(name + "\n")
        
        return True

# Run the menu task, or end it, according to user selection
menu_task = menu()

while menu_task == True:
    print("\nDo you wish to try again? (y/n)")
    i = input("> ")
    if i.lower() == "y" or i.lower() == "yes" or i.lower() == "true":
        menu_task = menu()
    else:
        exit()
    
    