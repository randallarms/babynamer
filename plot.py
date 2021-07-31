#======================================#
#              BabyNamer               #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# This program outputs a matplotlib/pyplot line graph of 
# a name's popularity over the years, based on the SSA data.

# Requires matplotlib. Install with "pip install matplotlib"
# or through your own preferred installation method.


# IMPORTS

import matplotlib.pyplot as plt
import objectify


# MENU

# Greeting text
print("\n\n=========")
print("BABYNAMER")
print("=========")
print("Open source @ github.com/randallarms/babynamer")

# Loop/exit input variables
loop_input = "yes"
loop_continue = ["yes", "y", "continue"]

# An incredibly constraining list of genders that are unfortunately necessary for this query
genders = ["male", "female", "m", "f", "boy", "girl"]
gender_male = ["male", "m", "boy"]
gender_female = ["female", "f", "girl"]

while loop_input in loop_continue:

    # PROMPT

    # Get the name
    print("\nWhich name do you wish to plot the popularity of? (NOTE: case-sensitive!) ")
    name = input("> ")

    # Get the gender
    print("\nWhich available gender do you wish to plot the popularity of? (Options: male, female) ")
    gender = input("> ")

    while not gender in genders:
        print("\nPlease enter one of the available options provided: \'male\' or \'female\'")
        print("\nWhich gender do you wish to plot the popularity of? (Options: male, female) ")
        gender = input("> ")


    # DATA

    # All data as an object
    __data__ = objectify.objectify()

    y_coords_male = []
    y_coords_female = []
    x_coords = []

    for __key__ in __data__['male'].keys():
        x_coords.append(int(__key__))
        if name in __data__['male'][__key__].values():
            for rank, name_val in __data__['male'][__key__].items():
                if name_val == name:
                    y_coords_male.append(1001-int(rank))
        else:
            y_coords_male.append(0)

    for __key__ in __data__['female'].keys():
        if name in __data__['female'][__key__].values():
            for rank, name_val in __data__['female'][__key__].items():
                if name_val == name:
                    y_coords_female.append(1001-int(rank))
        else:
            y_coords_female.append(0)


    # PLOT

    # Create line graph
    plt.figure(num='Popularity of ' + name)
    plt.title('Popularity of \"' + name + '\"')

    # Plot the coords
    if gender in gender_male:
        y_coords = y_coords_male
    if gender in gender_female:
        y_coords = y_coords_female

    plt.plot(x_coords, y_coords, marker=',')
        
    # Build x, y axes
    plt.xlabel('Year')
    plt.ylabel('Rank')
    plt.yticks([1000, 900, 800, 700, 600, 500, 400, 300, 200, 100, 1], ["#1", "#100", "#200", "#300", "#400", "#500", "#600", "#700", "#800", "#900", "#1000"])

    # Build line graph
    plt.grid(True)

    # Display line graph
    plt.show()

    # Prompt to continue
    print("\nWould you like to look up another name? ")
    loop_input = input("> ")
