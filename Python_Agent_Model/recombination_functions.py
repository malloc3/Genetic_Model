# THis file is to manage the different types of mutations.   THis is complcated and could be very difficult to get right.
# A broad yet important axiom for this entire file is that the actions of one Sister Chromatid do not affect the actions of others
# There are 4 typse of Reombination that can occur in this version of the model.
    # Gene Conversion Swap (wehere two genes trade places)
    # Gene Conversion Replace (Where one gene is copied to another chromosome)
    # Tail Swap (where a gene and everything below that gene is swapped between two chromsoomes)
    # Tail Replace (Where a gene and everythign below that gene is replaced with a copy from another chromosome)


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




# ================== Non Reciprical Recombination ==================== #
# This is largely written such that it can hace a TON of flexibility.
# The way that params are passed down and the way that the "mean" could be anythign
# and how the functions used for calculating mean and for performing teh recombination are flexible
# you can make this do pretty much anything.
# The way this is written it is a percentage of the total number of genes not of the total Base Pairs.
#
#
# This performs the non_reciprical recombination events based on the params given.
# You can modify how the mean is calculated biased for the number of chromosomes in a sister chromatid etc 
""" recombination_function = mutation_functions.poisson
non_reciprical_recombination_params = {
    "function": mutation_functions.poisson, # The function for calculating how many recombination events with some mean
    "mean": .25, # e.g. mean 2 mean number or recombination events
    "biased_mean_function": np.multiply, # None if want a consistant mean across all chromatids.  The function that biases the mean on the number of chromosomes in the chromatid
    "percentage_of_chromosomes_swap": .25, #How much of the chromosome is swapped per recombination event
    "percentage_function": None #If none then the percentage is constant.  Otherwise will be chosen from the function
} """
def non_reciprical_recombination(sis_chroma, global_params):
    if len(sis_chroma.chromosomes) < 2:
        warnings.warn('There is less than two Chromosomes.  Recombinatin Not possible')
        return #Cannot continue with this if there is only 1 chromosomes
    params = dict.copy(global_params) #makes a shallow copy of the params so we don't edit original
    # Sets all the sis chroma params corretly
    params['calc_recombination_events_params']['sis_chroma'] = sis_chroma
    params['chromosome_selection_params']['sis_chroma'] = sis_chroma
    params['gene_selection_params']['sis_chroma'] = sis_chroma

    #Gets the number of recombination events to occur per sister_chromatid
    num_of_recombinations = params["calc_recombination_events_func"](params["calc_recombination_events_params"])

    for recomb in range(0, num_of_recombinations):
        chromo1, chromo2 = params['chromosome_selection_func'](params["chromosome_selection_params"])
        # Update the parameters with the chromosome info
        params["gene_selection_params"]["chromo1"] = chromo1
        params["gene_selection_params"]["chromo2"] = chromo2
        gene_position_1, gene_position_2 = params["gene_selection_func"](params["gene_selection_params"])
        for (gp1, gp2) in zip(gene_position_1, gene_position_2):
            dna_functions.replace_gene(chromo1, chromo2, gp1, gp2)





# THis will return two lists Gene1 list and Gene2 list.  Each list will have a list of positions in chromo1 and chromo2 (respectivly)
# That will be switche with eachother.  This list will actually be a copy of each other since they should be grouped
#  THe number of genes will be rounded close to the percentage of teh genome total number of genes to be swapped
#
# Input
#   params = {
#       "percentage": 0.1,
#        "sis_chroma": Chromosome, #This will be passed and upadated each time
#        "chromo1": None, #This will be passed and updated each time
#        "chromo2": Chromosome  #This will be passed and updated each time
#   }
def simple_consecutive_percentage(params):
    chromo1 = params["chromo1"]
    chromo2 = params["chromo2"]
    percent = params["percentage"]
    number_of_selected_genes = round(percent * len(chromo1.genes))
    gene_position_1 = select_random_consecutive_positions(len(chromo1.genes), number_of_selected_genes)
    gene_position_2 = list(gene_position_1)
    return([gene_position_1, gene_position_2])
    

# Selects a random consecutive position throughout the genome matching some length given
#
# Input
#   list_len = Int the length of the list
#   num_items = Int the number of consecutive items to grab
def select_random_consecutive_positions(list_len, num_items):
    if num_items > list_len:
        raise ValueError("num_items is greater than the length of the list")
    
    start_index = random.randint(0, list_len - num_items)
    return range(start_index, start_index+num_items)


# Selects two random chromosomes from the sister chromatid that is in the param 
# Input
#   param = {"sis_chroma": Sister_Chromatid}
#
# Output
#   List [Chromo1, Chromo2]
def two_random_chromosomes(params):
    sis_chroma = params['sis_chroma']
    if len(sis_chroma.chromosomes) < 2:
        raise Exception('There is less than two Chromosomes.')
    
    #Gota make a shallow copy so we don't edit OG list
    chromosomes = list(sis_chroma.chromosomes)
    chromo1 = random.choice(chromosomes)
    chromosomes.remove(chromo1)
    chromo2 = random.choice(chromosomes)
    return([chromo1, chromo2])

        

# This performs the non_reciprical recombination events on multiple cells
def non_reciprical_recombination_cels(cels, params):
    for cel in cels:
        non_reciprical_recombination_cel(cel, params)

def non_reciprical_recombination_cel(cel, params):
    for sis_chroma in cel.sister_chromatids:
        non_reciprical_recombination(sis_chroma, params)


# ==================== End Non Reciprical Recombination ==================#



#  =================== Gene Swap ========================================#
# TODO_NOT COMPLETE
# TODO.  This should return a list of chromosomes and genes that need to swap.
#  Figuring this out is super complicated.......
def gene_swap_simple_poisson(params):
    raise Exception("This function is not completed")

# This defines the frequency of a simple gene conversion swap to occur.
#  This frequency is highly dependent on the function and params given.
#
# The function will determine which 
def gene_conversion_swap(sis_chroma, function, params):
    # Some functions may need to know specific relationships between genes and cells.  It is unown at this time but this info should be available
    params["sis_chroma"] = sis_chroma

    #THis function will return a list of lists including [[chromosome1, chromosome2, gene_location1, gene_location2], ....] for each swap that will occur
    genes_to_swap = function(params)
    for g_swap in genes_to_swap:
        dna_functions.swap_two_genes(g_swap[0], g_swap[1], g_swap[2], g_swap[3])


# This applys the simple gene conversion swap to a specific cel
# THis method does not account for how gene swapping could affect other types of recombination
def simple_gene_conversion_swap_cels(cels, function, params):
    for cel in cels:
        for sis_chroma in cel.sister_chromatids:
            gene_conversion_swap(sis_chroma, function, params)

#  =================== End Gene Swap ========================================#



#  =================== depricated] ========================================#
# Chooses two random chromosomes to randomly do a recombination event
#
# Input
#   sis_chromatids = Class sister_chromatids
def random_recombination(sis_chromatid):
    
    # Must make a shallow copy of the list.  So we can modify the list locally 
    # but keep the sam objects inside the list!  Important!
    possible_chromosomes = list(sis_chromatid.chromosomes)

    
    if len(possible_chromosomes) <= 1: #there is only 1 chromosome
        warnings.warn("recombination_even_not_possible")
    else: # there are more than 2 chromosomes
        chromo_1 = random.choice(possible_chromosomes) #Random choice chromosome
        
        #Randomly choose chromosome that is NOT chromo 1
        possible_chromosomes.remove(chromo_1)
        chromo_2  = random.choice(possible_chromosomes)

        dna_functions.random_recombination(chromo_1, chromo_2)