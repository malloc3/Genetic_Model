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


# This defines the frequency of a gene conversion swap to occur.
#  This frequency is highly dependent on the function and params given.
#
# This function will add the number of chromosomes, and the 
def gene_conversion_swap(sis_chroma, function, params):
    print("do something")


# The details of exactly how this handles stuff is hard to decide....
def recombinate_sister_chromatid(params):
    print("do something")

# This will manage the recombination of the sister_crhomatids of a cell.
def recombinate_cel(cel, recombination_params):
    for sis_chroma in cel.sister_chromatids:
        recombinate_sister_chromatid(recombination_params)


def recombinate_cels(cels, recombination_params):
    for cel in cels:
        recombinate_cel(cel, recombination_params)


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