# This libraary holds helpful functions for dealing with dna!
import numpy as np # type: ignore
import random
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *
from enum import Enum
import uuid

# The shortest we will allow a gene to be.  This is moderatly arbitrary
shortest_possible_gene = 3


# This generates a random choice for a base pair
# Return
#   Bp = Bp basepair class.   A specific basepair
def random_bp():
    bp = random.choice(bp_options())
    return(Bp[bp])


# THis duplicates a chromosome with it's genes etc but makes a new exact copy
# Input
#   chromo = Chromosome  the chromosome to be duplicated
#
# Return
#   dup_chromo = Chromosome a chromosome that is an exact copy of the input chromosome
def duplicate_chromosome(chromo):
    new_genes = [duplicate_gene(g) for g in chromo.genes]
    dup_chromo = chromosome(new_genes, id = uuid.uuid1(), parent = chromo.id)
    return(dup_chromo)

# Duplicates a gene.  Makes an exact copy of a gen but as a new object
#
# Input 
#   gene = Gene class the gene to duplicate
# Output
#   dup_gene = the new duplicated gene
def duplicate_gene(gen, id = uuid.uuid1()):
    old_bp = gen.sequence
    new_bp = [duplicate_bp(b) for b in gen.sequence]
    return(gene(new_bp, id, parent = gen.id, position = gen.position))


# Duplicates a base pair.   Makes an exact copy of the bp
# Input
#  b = Class Base Pair.
#
# OUtput
#  dup_bp = Class Base Pair.  The new base pair
def duplicate_bp(b):
    return(Bp[b.name])




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
                          std_dev_percent_of_ave_gene = 0.4,
                          chromo_id = uuid.uuid1(),
                          chromo_parent = None):
    std_dev = average_gene_length * std_dev_percent_of_ave_gene
    bp_count = 0
    genes = []
    gene_position = 0
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

        # Essentially we don't want genes that are absurdly short
        if gene_length > shortest_possible_gene:
            genes.append(create_basic_gene(gene_length, position = gene_position)) #append a new gene
        gene_position += 1
    return(chromosome(genes, chromo_id, chromo_parent))



        
# This generates a basic gene!
# Input
#   length = INT the length of the gene!
#
# Output
#   gene = The gene that was generated!
def create_basic_gene(length, id = uuid.uuid1(), parent = None, position = None):
    sequence = [random_bp() for _ in range(length)]
    return(gene(sequence, id, parent, position))


# Randomly recombinates a genes from these chromosomes
#  Essentially choose a gene at random and then switches them!
#
# Input
#   chromo1 = Class Chromosome
#   chromo2 = Class Chromosome
def random_recombination(chromo1, chromo2):
    if len(chromo1.genes) != len(chromo2.genes):
        raise ValueError("Chromosomes that should be the same number of genes are not :(")
    else:
        #gets the genes from random location in chromosome
        gene_location = random.randint(0, len(chromo2.genes)-1)
        
        #Swaps the genes
        swap_two_genes(chromo1, chromo2, gene_location, gene_location)

        #Updates teh chromosomes with the id of the chromosome it swaped with
        chromo1.add_recombination(chromo2.id)
        chromo2.add_recombination(chromo1.id)


# This swabs two genes between two chromosomes. And updates the genes to their new position idicies
#
# Chromo_1 = Class Chromosome 
def swap_two_genes(chromo1, chromo2, gene_position_1, gene_position_2):
    gene_location = random.randint(0, len(chromo2.genes)-1)
    gene_1 = chromo1.genes[gene_position_1]
    gene_2 = chromo2.genes[gene_position_2]
    gene_1.position = gene_2.position
    gene_2.position = gene_1.position

    chromo1.genes[gene_position_1] = gene_2
    chromo2.genes[gene_position_2] = gene_1