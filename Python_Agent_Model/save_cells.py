import csv
import os
import pandas as pd





#TODO make this faster to write by using pandas??  I don't think the hold up in generation
# Times is from writing though.  Actually certainly not.

std_headers = ['Strain_ID', 'Parent_ID', 'Generation', "number_of_chromatids", #Cell Info
                "chromatid_number", "CC_Number", "chromatid_id", "chromatid_parent",    # Chromatid INfo
               "chromosome_id", "chromosome_parent", "chromsome_recombinations", "chromosome_length", "chromo_num_genes",    # Chromosome INfo
               "gene_id", "gene_parent", "gene_position", # GEne Info
               "Sequence_str"] # GEne Sequence
# This module is to handle saving the cells in a logical and helpful way
#  Thie should probably save stuff to a CSV or similar.


# THis writes a generation to a given dataframe
#
#Input
#   df = Pandas DF that stuff will be written to
#   generation = List of the cells in the gerenation
def write_generation_to_df(df, generation):
    generation_data = []
    for cel in generation:
        generation_data += get_cell_data_to_write(cel)
    temp_df = pd.DataFrame(generation_data, columns=std_headers)
    return(pd.concat([df, temp_df], ignore_index=True))


#This saves the current generation to a CSV designated in the FILE LOCATION
#
# Input
#    generation = List of class Cell to be written
#   file_name = String the file name of the file where the data will be written.
def write_generation(generation, file_name):
    all_data = []
    for cel in generation:      # This part take a LONG time.   Not sure how to optimize that part.
        all_data += get_cell_data_to_write(cel)
    temp_df = pd.DataFrame(all_data, columns=std_headers)
    temp_df.to_csv(file_name, mode='a', header=False, index=False)  #This also takes some time.  So it may be good to offload this once per run


# Pulls relevant data from the cell and reports it as a list of lists
def get_cell_data_to_write(cel):
    cell_info = []
    # get the cell Information
    strain_id = cel.id
    parent_id = cel.parent
    generation = cel.generation
    number_of_chromatids = cel.number_chromatids()

    # Now we gotta get chromatid information
    for sis_chroma in cel.sister_chromatids:
        chromatid_number = sis_chroma.chromatid_number
        cc_number = len(sis_chroma.chromosomes)
        chromatid_id = sis_chroma.id
        chromatid_parent = sis_chroma.parent

        #Now lets get individual chromosome information
        for chromo in sis_chroma.chromosomes:
            chromosome_id = chromo.id
            chromosome_parent = chromo.parent
            chromosome_recombinations = chromo.recombination
            chromosome_length = chromo.length
            chromosome_num_genes = len(chromo.genes)

            #Now lets get individual gene information
            for ge in chromo.genes:
                gene_id = ge.id
                gene_parent = ge.parent
                gene_position = ge.position
                sequence_str = ge.sequence_str()
                cell_info.append([strain_id, parent_id, generation, number_of_chromatids,
                                  chromatid_number, cc_number, chromatid_id, chromatid_parent,
                                  chromosome_id, chromosome_parent, chromosome_recombinations, chromosome_length, chromosome_num_genes,
                                  gene_id, gene_parent, gene_position,
                                  sequence_str])
    return(cell_info)



# This opens an existig csv or creates and formates a new one
# Then writes the each cell in the generation to the csv
def write_generation_to_csv(generation, filename, metadata = None):
    #makes the file if it doesnt exist
    if not os.path.exists(filename):
        write_new_file_with_metadata(filename, metadata)
    write_generation(generation, filename)

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