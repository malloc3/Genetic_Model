import csv
import os





#TODO make this faster to write by using pandas??  I don't think the hold up in generation
# Times is from writing though.  Actually certainly not.

std_headers = ['Strain_ID', 'Parent_ID', 'Generation', "chromosome_number", "CC_Number", "Sequence_str"]
# This module is to handle saving the cells in a logical and helpful way
#  Thie should probably save stuff to a CSV or similar.

#This saves the current generation to a CSV designated in the FILE LOCATION
#
def write_generation(generation, writer):
    all_data = []
    for cel in generation:
        all_data += get_cell_data_to_write(cel)
    #[get_cell_data_to_write(cel) for cel in generation] #NEED TO REWRITE THIS
    writer.writerows(all_data)


#Dictates what data is writen to the csv for all writer functions
# TODO SHOULD MANAGE CHROSOME NUMBER A LITTLE BETTER PROBABLY
def get_cell_data_to_write(cel):
    cell_chromosome_sequences = []
    sis_chroma_number = 0
    for sis_chroma in cel.sequence_str():
        sis_chroma_number += 1 #For iterator
        CC_number = len(sis_chroma)
        for chromo_seq in sis_chroma:
            cell_chromosome_sequences.append([cel.id, cel.parent, cel.generation, sis_chroma_number, CC_number, chromo_seq])
    return(cell_chromosome_sequences)



# This opens an existig csv or creates and formates a new one
# Then writes the each cell in the generation to the csv
def write_generation_to_csv(generation, filename, metadata = None):
    #makes the file if it doesnt exist
    if not os.path.exists(filename):
        write_new_file_with_metadata(filename, metadata)

    #Writes actual files
    with open(filename, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        write_generation(generation, writer)

# This opens an existig csv or creates and formates a new one
# Then writes the cell information to the csv
def write_cel_to_csv(cel, filename, metadata = None):
    #makes the file if it doesnt exist
    if not os.path.exists(filename):
        write_new_file_with_metadata(filename, metadata)
    
    # Write new data to file
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(get_cell_data_to_write(cel))


# This will create and write a file with metadata for later log files
#
# Input
#   filename = STRING the name of the file
#   metadata = DICTIONARY
#       {
#           mutation_mean_rate: .5,
#           mutation_mean_std: 1,
#           max_generation_size: 600,
#           death_rate: 0.2
#       }
def write_new_file_with_metadata(filename, metadata):
    if os.path.exists(filename):
        raise Exception("Log file filename already exists. Cannot OVerwite: " + filename)
    else:
        if not metadata: raise Exception("Metadata is none")    
        with open(filename, 'w', newline='') as csvfile:
            #Adds all our metadata to the file
            fieldnames = metadata.keys()
            dict_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            dict_writer.writeheader()
            dict_writer.writerow(metadata)

            #adds the headers for the real data
            regular_writer = csv.writer(csvfile)
            regular_writer.writerow(std_headers)
        print(f"Created file '{filename}'")