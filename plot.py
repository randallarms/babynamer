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

# Get the name
print("\nWhich name do you wish to plot the popularity of? (NOTE: case-sensitive!) ")
__name__ = input("> ")


# DATA

# All data as an object
__data__ = objectify.objectify()

y_coords_male = []
y_coords_female = []
x_coords = []

for __key__ in __data__['male'].keys():
    x_coords.append(int(__key__))
    if __name__ in __data__['male'][__key__].values():
        for rank, name_val in __data__['male'][__key__].items():
            if name_val == __name__:
                y_coords_male.append(int(rank))
    else:
        y_coords_male.append(0)
for __key__ in __data__['female'].keys():
    if __name__ in __data__['female'][__key__].values():
        for rank, name_val in __data__['female'][__key__].items():
            if name_val == __name__:
                y_coords_female.append(int(rank))
    else:
        y_coords_female.append(0)


# PLOT

# Create line graph
plt.figure(num='Popularity of ' + __name__)
plt.title('Popularity of \"' + __name__ + '\"')

# Plot the coords
plt.plot(x_coords, y_coords_male, marker=',')
    
# Build x, y axes
plt.xlabel('Year')
plt.ylabel('Rank')
plt.yticks(range(0, 1001, 100), range(0, 1001, 100))

# Build line graph
plt.grid(True)

# Display line graph
plt.show()