import random
from cells import *
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *
from sister_chromatids import *
import dna_functions
import sister_chromosome_functions
import uuid

#Creates a basic cell from input parameters
#
# Input
#  params = list of dictionaries.
#    number of items in the list = number of chromosomes
#       each item in the list should be a list of
#    [ 
#       dict{
#           "chromo_length" = LENGTH OF THE CHROMOSOMES
#           "ave_gene_lenth" = average length of the genes
#           "chromo_count" = the number of chromosomes in the sister chromatids
#       }
#    ]
def create_basic_cell(params, ID, parent_ID = "na"):
    sis_chroma_list = []
    for sister_chromo_info in params:
        chromo_length = sister_chromo_info['chromo_length']
        ave_gene_length = sister_chromo_info['ave_gene_length']
        chromo_count =sister_chromo_info['chromo_count']
        sis_chroma = sister_chromosome_functions.generate_basic_chromatid(chromo_length, 
                                                             ave_gene_length,
                                                             chromo_count)
        sis_chroma_list.append(sis_chroma)
    return(Cell(ID, sis_chroma_list, parent_ID))


#This duplicates a cell exactly!  Makes new objects for everythign but they are
# exact copies of the original (like if meosis was perfect!)
# Input
#   cel = Cell class the cell that should be duplicated
#
# OUtput
#   dup_cell = the new cell that is duplicated!
def duplicate_cell(cel, ID):
    sis_chromo = [sister_chromosome_functions.duplicate_sister_chromatid(sis_chromo) for sis_chromo in cel.sister_chromatids]
    dup_cel = Cell(ID, sis_chromo, cel.id, generation = cel.generation + 1)
    return(dup_cel)


# This duplicates the parent cell exactly and give the new cells unique ids generated
#  by the UUID function.
#
# Input
#   parent_cel = Cell class the parent that needs to be duplicated
#
# Output
#   daughter_cells = List of daughter cells that are exact duplicates of parent
def multiple_duplicates_with_UUID(parent_cel, number_of_duplicates):
    daughter_cells = []
    for i in range(number_of_duplicates):
        daughter_cells.append(duplicate_cell(parent_cel, uuid.uuid1()))
    return(daughter_cells)


# This manages the cell mutations protocols.  THe functions of this are yet undefined.
#
def mutate_cell(cel):
    return(cel)

# THis helps mutate many cells.   Unknown function at this time.
def mutate_cells(cels):
    return([mutate_cell(cel) for cel in cels])
