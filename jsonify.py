#======================================#
#            BabyNamer Sort            #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# The program returns a JSON version of the SSA data based on input parameters.

import os
import json
import objectify

# Write the JSON to a local file
with open("data.json", "w") as outfile:
    json.dump(objectify.objectify(), outfile, indent=4)