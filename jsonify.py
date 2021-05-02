#======================================#
#              BabyNamer               #
#           by Randall Arms            #
#  github.com/randallarms/babynamer    #
#======================================#

# This program outputs a JSON file containing the objectified SSA data.

import json
import objectify

# Write the JSON to a local file
with open("data.json", "w") as outfile:
    json.dump(objectify.objectify(), outfile, indent=4)