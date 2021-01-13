#======================================#
#            BabyNamer Sort            #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# The program takes the ordered list of popular boy and girl names from the SSA and sorts it for use with the main program.
# Ya know, because I am not manually sorting two lists of 1000 names for every single year. >:)

import os

# Opening text
print("\n\n==============")
print("BABYNAMER SORT")
print("==============")
print("Sorting names...")

    
# Get files
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

year = "2018"

names = open(os.path.join(__location__, "names/" + year + "/unsorted.txt"), "r")

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

print("Sorting done!")