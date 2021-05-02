#======================================#
#              BabyNamer               #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# This program returns an object version of the SSA data.

import os

# Get file location
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
__names_location__ = os.path.join(__location__, "names/")

# Create a JSON-friendy dict
def objectify():
    data = {}
    years = [] 
    years_dict = {}
    contents = os.listdir(__names_location__)

    # Find all year directories
    for item in contents:
        years.append(item)
        years_dict[item] = {}

    # Add the available years to the nested dict of each gender in data
    data['male'] = years_dict.copy()
    data['female'] = years_dict.copy()

    # Add each year's names to the data object
    for year in years:
        __year_location__ = os.path.join(__names_location__, year + "/")  
        __unsorted_location__ = os.path.join(__year_location__, "unsorted.txt")
        names = open(__unsorted_location__, "r")

        # Fill list of possible names from file
        male_year_names = {}
        female_year_names = {}
        for line in names:
            name_parts = line.split()
            n = int(name_parts[0])-1
            male_year_names[n] = name_parts[1]
            female_year_names[n] = name_parts[2]
        names.close()
        
        data['male'][year] = male_year_names.copy()
        data['female'][year] = female_year_names.copy()
    
    # Return the data dict
    return data