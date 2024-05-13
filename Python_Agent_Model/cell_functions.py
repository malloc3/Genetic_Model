import random
from cells import *
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *
from sister_chromatids import *
import dna_functions
import sister_chromosome_functions
import uuid
import numpy as np
import warnings
import mutation_functions


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
def create_basic_cell(params, ID, parent_ID = None, generation = None):
    sis_chroma_list = []
    chroma_num = 0
    for sister_chromo_info in params:
        chromo_length = sister_chromo_info['chromo_length']
        ave_gene_length = sister_chromo_info['ave_gene_length']
        chromo_count =sister_chromo_info['chromo_count']
        sis_chroma = sister_chromosome_functions.generate_basic_chromatid(chromo_length, 
                                                             ave_gene_length,
                                                             chromo_count, chromatid_number = chroma_num)
        sis_chroma_list.append(sis_chroma)
        chroma_num += 1
    return(Cell(ID, sis_chroma_list, parent_ID, generation))


#This duplicates a cell exactly!  Makes new objects for everythign but they are
# exact copies of the original (like if meosis was perfect!)
# Input
#   cel = Cell class the cell that should be duplicated
#
# OUtput
#   dup_cell = the new cell that is duplicated!
def duplicate_cell(cel, ID=None):
    if not ID:
        ID = uuid.uuid1()
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
        daughter_cells.append(duplicate_cell(parent_cel))
    return(daughter_cells)


#TODO Create the function that manages recombination
# This has no knowledge of how many chromosomes a chromatid has.
#  It will chose chromatids at random.  #TODO THIS PROBABLY NEEDS TO BE DIFFERENT
#
# Input
#   cels = List of all the cells in a generation
#   params = Dictionary
#   {
#       recombination_probability: [3, .001] # The normal curve about mean that variation will happen
#   }
def recombinate_cells_norm(cels, params):
    for cel in cels:
        recombination_probability = params["recombination_probability"]

        number_of_recombination_events = abs(round(np.random.normal(recombination_probability[0], recombination_probability[1])))
        for i in range(number_of_recombination_events):
            recombinate_random_chromatid(cel)


# Randome recombines a two chromsomes in a random chromatid
#
# Input
#   cel = cell class
def recombinate_random_chromatid(cel):
    random_sis_chroma = random.choice(cel.sister_chromatids)
    sister_chromosome_functions.random_recombination(random_sis_chroma)


# TODO
#  Need to think on this.   I have the normal about zero.  Such that neg
# numbers are equally as likely as positive numbers.  Negs are considered teh same
#  as positive (e.g. abs(nrom))   THis makes a change twice as likely....
#
#
# This will decide if a cell will or will not unergo CCNV
# If it does happen it will happen to a random chromosome.
#Input
#   cels = List of all the cells in a generation
#   params = Dictionary
#   {
#       variation_probability: [0, .001] # The normal curve about mean that variation will happen
#       probability_of_pos: 0.5 #likelyhood any change will be positive (inverse for neg)
#
#   }
def ccnv_cels_norm(cels, params):
    for cel in cels:
        # Get param values
        variation_probability = params["variation_probability"]
        probability_of_pos = params["probability_of_pos"]
    
        #Check that param values are acceptable
        if not (0 <= probability_of_pos <= 1):
            raise ValueError("Probability of Positive must be between 0 and 1.")



        # Gets the number of times that a chromosome will change in a cell
        # This should be a rare event
        # Normal disdribution around 0 should make UP and DOWN equally likely
        number_of_chromosome_changes = abs(round(np.random.normal(variation_probability[0], variation_probability[1])))
        
        # We will randomly choose a sister chromatid to vary up or down x number of times
        for i in range(number_of_chromosome_changes):
            sis_chroma = random.choice(cel.sister_chromatids)

            # Doesnt allow it to go below 1 chromosome.  Does increase the chance that a
            # chromosome that is at 1 ill go up compaired to other chromosome counts #TODO
            if len(sis_chroma.chromosomes) <= 1:
                result = 1
            else:
                outcomes = [1, -1]
                weights = [probability_of_pos, 1 - probability_of_pos] 
                result = random.choices(outcomes, weights=weights, k=1)[0]
            if result == 1: #positive change
                sister_chromosome_functions.add_random_chromosome(sis_chroma)
            elif result == -1: #Negative change
                sister_chromosome_functions.remove_random_chromosome(sis_chroma)
            else: #THIS SHOULD NEVER HAPPEN BUT GOTTA CATCH THEM ALL
                raise ValueError("The results of pos v neg are inconclusive?")




# This creates point mutations in the Genome with some frequency determiend by the function and function params
# The frequency is on a CELL basis with no BP or cell specific relative frequency of mutations.  The chromosomes
# that have more copies are more likely to see a mutation due to the increased number of copies.  THis is linear.
# Input:
#   cels = List of Cels
#   function = Function determining the frequence of point mutations in a specific cell
#   function_params = List of params for the function above
# Output
#   None
def randomly_distributed_point_mutate_cell(cel, function, function_params):
    number_of_mutation = function(function_params) #This should give the number of mutations
    for i in range(number_of_mutation):
        try:
            # Gets a random chromatid from the chromatids in the cell
            ran_chroma = random.choice(cel.sister_chromatids)

            # Gets a random chromosome from the chromatid
            ran_chromo = random.choice(ran_chroma.chromosomes)
            ran_gene = random.choice(ran_chromo.genes) # Gets a random gene from chromosome
            ran_bp = random.choice(ran_gene.sequence) #Gets a random BP to mutate
        except IndexError:
            print(ran_chromo.length())
            raise Exception("Genes or Sequences have length of Zero.  This cannot be allowed to happen")
        ran_bp.bp = random.choice(dna_functions.bp_options()) #Replaces with a random BP
    return(cel)


# This will randomly mutate the cels in the list cels per the frequencey given by the function and function params
#
# Input:
#   cels = List of Cels
#   function = Function determining the frequence of point mutations in a specific cell
#   function_params = List of params for the function above
# OUtput
#   None
def randomly_distributed_point_mutate_cells(cels, function, function_params):
    return([randomly_distributed_point_mutate_cell(cel, function, function_params) for cel in cels])











# ==================  Depricated ============================= #
# Genomes should have higher mutation rates.
#
#
# This mutates on a normal distribution.  The distribution dictates
# how many point mutations will occur across the whole cell.
#  These mutations will then RANDOMLY occur somehwere in the genome
#
# params[0] = mean
# params[1] = standard deviation
def point_mutate_cell_norm(cel, params):
    number_of_mutations = mutation_functions.rounded_norm(params[0], params[1])
    for i in range(number_of_mutations):
        try:
            # Gets a random chromatid from the chromatids in the cell
            ran_chroma = random.choice(cel.sister_chromatids)

            # Gets a random chromosome from the chromatid
            ran_chromo = random.choice(ran_chroma.chromosomes)
            ran_gene = random.choice(ran_chromo.genes) # Gets a random gene from chromosome
            ran_bp = random.choice(ran_gene.sequence) #Gets a random BP to mutate
        except IndexError:
            print(ran_chromo.length())
            raise Exception("Genes or Sequences have length of Zero.  This cannot be allowed to happen")
        ran_bp.bp = random.choice(dna_functions.bp_options()) #Replaces with a random BP
    return(cel)

# THis helps mutate many cells.
# The mutation of the cell is based on the normal distribution
# parameterized by the given params
#
# params[0] = mean
# params[1] = standard deviation
def point_mutate_cells_norm(cels, params):
    return([point_mutate_cell_norm(cel, params) for cel in cels])
