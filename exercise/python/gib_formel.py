#!/bin/python

import sys
import os
import json

# Input:
# $1 = vilka atomer (atomslag)
# $2 = Massprocent

periodic_table_path = "/home/simon/skola/CHI/other/periodic_table_minimal.json"

periodic_table = json.load(open(periodic_table_path, "r"))

atoms = []
count = 0

##########################################################################################################################
# Input preparation:
##########################################################################################################################

try:
    atom_string = sys.argv[1]
except:
    print("Please enter the atom types space separated, in a string, as the first argument")

try:
    massprocent = sys.argv[2]
except:
    print("Please enter the mass percentages space separated, in a string, as second argument")



def atom_input(atom_string):
    atom_list = atom_string.split()
    print(atom_list)

    for i in atom_list:
        for j in range(0, 118):
            print(j, periodic_table["elements"][j]["symbol"])

            if i == periodic_table["elements"][j]["symbol"]:
                atoms.append([i, periodic_table["elements"][j]["atomic_mass"]])
                break


    return atoms

##########################################################################################################################
# Logic:
##########################################################################################################################



##########################################################################################################################
# Output:
##########################################################################################################################

print("comprehensible atom list:", atom_input(atom_string))

# for i in range(0, 10):
#      print(f"name: {periodic_table['elements'][i]['symbol']}, state: {periodic_table['elements'][i]['phase']}")

print(sys.argv)

