# This libraary holds helpful functions for dealing with dna!
import numpy as np # type: ignore
import random
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *


# This generates a random choice for a base pair
# Return
#   Bp = Bp basepair class.   A specific basepair
def random_bp():
    bp = random.choice(["a", "c", "g", "t"])
    return(Bp(bp))


# THis duplicates a chromosome with it's genes etc but makes a new exact copy
# Input
#   chromo = Chromosome  the chromosome to be duplicated
#
# Return
#   dup_chromo = Chromosome a chromosome that is an exact copy of the input chromosome
def duplicate_chromosome(chromo):
    new_genes = [duplicate_gene(g) for g in chromo.genes]
    dup_chromo = chromosome(new_genes)
    return(dup_chromo)

# Duplicates a gene.  Makes an exact copy of a gen but as a new object
#
# Input 
#   gene = Gene class the gene to duplicate
# Output
#   dup_gene = the new duplicated gene
def duplicate_gene(gen):
    old_bp = gen.sequence
    new_bp = [duplicate_bp(b) for b in gen.sequence]
    return(gene(new_bp))


# Duplicates a base pair.   Makes an exact copy of the bp
# Input
#  b = Class Base Pair.
#
# OUtput
#  dup_bp = Class Base Pair.  The new base pair
def duplicate_bp(b):
    return(Bp(b.bp))




# This generates a chromosome
# Input
#   length = how long in Base Pairs the chromosomes needs to be.
#   average_gene_length =  INT The average length of the genes!
#   std_dev_percent_of_mean = DOUBLE  the percentage of the mean length the 
#                               standard deviation will be set at for average 
#                               gene lengths.  Longer teh average the more the
#                               genes should deviate from mean.
#
# Output
#   chromo = The chromosome it Generates!
def make_baisc_chromosome(chromo_length, 
                          average_gene_length, 
                          std_dev_percent_of_ave_gene = 0.4):
    std_dev = average_gene_length * std_dev_percent_of_ave_gene
    bp_count = 0
    genes = []
    while bp_count < chromo_length:
        #Get a random length for the gene 
        gene_length = round(np.random.normal(average_gene_length, std_dev))

        # Make sure that the addition of this gene won't make it longer than 
        # The chromosome.
        #  TODO this is kinda an issue since all the genes at the ends will be
        #       short...  Which is not realistic
        if bp_count + gene_length > chromo_length:
            gene_length = chromo_length - bp_count   
            
        bp_count += gene_length #Iterate
        genes.append(create_basic_gene(gene_length)) #append a new gene
    return(chromosome(genes))



        
# This generates a basic gene!
# Input
#   length = INT the length of the gene!
#
# Output
#   gene = The gene that was generated!
def create_basic_gene(length):
    sequence = [random_bp() for _ in range(length)]
    return(gene(sequence))

