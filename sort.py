#======================================#
#            BabyNamer Sort            #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# The program takes the ordered list of popular boy and girl names from the SSA and sorts it for use with the main program.
# Ya know, because I am not manually sorting two lists of 1000 names each for every single year. >:)

import os

# Get file location
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__names_location__ = os.path.join(__location__, "names/")

# Get years that need sorting
years = [] 
contents = os.listdir(__names_location__)

for item in contents:
    __male_names_location__ = os.path.join(__names_location__, item + "/male.txt")
    __female_names_location__ = os.path.join(__names_location__, item + "/female.txt")
    
    if not os.path.isfile(__male_names_location__) and not os.path.isfile(__female_names_location__):
        years.append(item)

# Sort each year directory
for year in years:
    names = open(os.path.join(__names_location__, year + "/unsorted.txt"), "r")

    # Fill list of possible names from file
    male = []
    female = []

    for line in names:
        name_parts = line.split()
        male.append(name_parts[1])
        female.append(name_parts[2])
        
    names.close()

    # Commit names to sorted file
    male_names = open(os.path.join(__location__, "names/" + year + "/male.txt"), "w")
    female_names = open(os.path.join(__location__, "names/" + year + "/female.txt"), "w")

    for line in male:
        male_names.write(line + "\n")
    for line in female:
        female_names.write(line + "\n")

    male_names.close()
    female_names.close()