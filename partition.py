#======================================#
#         BabyNamer Partition          #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# This program creates a directory for the range of years specified, and adds a 
# blank text document named "unsorted" to each one, so I don't have to do it manually. >:)

import os

# Get file location and contents
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__names_location__ = os.path.join(__location__, "names/")
contents = os.listdir(__names_location__)

# Create directories
y1 = 1900
y2 = 2021

for y in range(y1, y2):
    __y_location__ = os.path.join(__names_location__, str(y) + "/")
    __unsorted_location__ = os.path.join(__y_location__, "unsorted.txt/")
    
    if not str(y) in contents:
        os.mkdir(__y_location__)
        unsorted = open(os.path.join(__y_location__, "unsorted.txt"), "w")
        unsorted.close()