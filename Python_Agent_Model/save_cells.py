import csv
import os

#TODO make this faster to write by using pandas??  I don't think the hold up in generation
# Times is from writing though.  Actually certainly not.

std_headers = ['Strain_ID', 'Parent_ID', 'Generation', "Sequence_str"]
# This module is to handle saving the cells in a logical and helpful way
#  Thie should probably save stuff to a CSV or similar.

#This saves the current generation to a CSV designated in the FILE LOCATION
#
def write_generation(generation, writer):
    all_data = [get_cell_data_to_write(cel) for cel in generation]
    writer.writerows(all_data)


#Dictates what data is writen to the csv for all writer functions
def get_cell_data_to_write(cel):
    return([cel.id, cel.parent, cel.generation, "SEQUENCe_NOT_AVAILABLE_YET"])



# This opens an existig csv or creates and formates a new one
# Then writes the each cell in the generation to the csv
def write_generation_to_csv(generation, filename):
    if not os.path.exists(filename):
        # If the file doesn't exist, create it and write to it
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(std_headers)
            write_generation(generation, writer)
        print(f"Created file '{filename}'")
    else:
        # If the file exists, read from it
        with open(filename, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            write_generation(generation, writer)

# This opens an existig csv or creates and formates a new one
# Then writes the cell information to the csv
def write_cel_to_csv(cel, filename):
    if not os.path.exists(filename):
        # If the file doesn't exist, create it and write to it
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(std_headers)
            writer.writerow(get_cell_data_to_write(cel))
        print(f"Created file '{filename}'")
    else:
        # If the file exists, read from it
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(get_cell_data_to_write(cel))