import numpy as np # type: ignore
import random
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *
from sister_chromatids import *
import dna_functions
import warnings

# Generates a chromosome and creates a sister chromatid set of "count" repeats.
# All chromosomes are identical
#
# Input:
#   chromosome = Class Chromosome the chromosome that should be copied
#   count = INT The number of sister chromatids it should have
#   length = how long in Base Pairs the chromosomes needs to be.
#   average_gene_length =  INT The average length of the genes!
#   std_dev_percent_of_mean = DOUBLE  the percentage of the mean length the 
#                               standard deviation will be set at for average 
#                               gene lengths.  Longer teh average the more the
#                               genes should deviate from mean.
#
# Output:
#   sister_chromo = CLass Sister_Chromatids 
def generate_basic_chromatid(chromo_length, 
                            average_gene_length, 
                            chromo_count,
                            std_dev_percent_of_ave_gene = 0.4):
    basic_chromo = dna_functions.make_baisc_chromosome(chromo_length, average_gene_length, 
                                                       std_dev_percent_of_ave_gene)
    return(basic_sister_chromatids_from_chromo(basic_chromo, chromo_count))
    

# Creats a sister chromatid set of "count" repeats from a given chromosome
# All chromosomes are identical
#
# Input:
#   chromosome = Class Chromosome the chromosome that should be copied
#   count = INT The number of sister chromatids it should have
#
# Output:
#   sister_chromo = CLass Sister_Chromatids 
def basic_sister_chromatids_from_chromo(chromo, count):
    chromosomes = [chromo]
    for i in range(count-1):
        chromosomes.append(dna_functions.duplicate_chromosome(chromo))
    
    return(sister_chromosomes(chromosomes))

 
# Adds a random chromosome from the list of chromosomes and updates list
def add_random_chromosome(sis_chromo):
    chromosome_to_duplicate = random.choice(sis_chromo.chromosomes)
    new_chromosome = dna_functions.duplicate_chromosome(chromosome_to_duplicate)
    sis_chromo.add_chromosome(new_chromosome)

# Removes a random chromosome fromthe sister chromosome
def remove_random_chromosome(sis_chromo):
    if len(sis_chromo.chromosomes) <= 1:
        warnings.warn("cannont make chromosome go below 1")
    else:
        chromo_to_remove = random.choice(sis_chromo.chromosomes)
        sis_chromo.remove_chromosome(chromo_to_remove)

# THis duplicates a sister chromatids with it's chromosomes etc but makes a new exact copy
# Input
#   chromo = Chromosome  the chromosome to be duplicated
#
# Return
#   dup_sister_chromo = Sister Chromosomes a suster chromosome that is an exact copy of the input sister chromosome
def duplicate_sister_chromatid(sis_chromo):
    chromos = [dna_functions.duplicate_chromosome(chromo) for chromo in sis_chromo.chromosomes]
    dup_sister_chromo = sister_chromosomes(chromos)
    return(dup_sister_chromo)


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