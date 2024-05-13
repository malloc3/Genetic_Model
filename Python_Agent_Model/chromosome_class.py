import random
from bp_class import *
from short_DNA_region_class import *

# This is a grouping of genes that creates a chromosome
#
# Each chromosome has some list of genes that make up it's length
# Length = number of BP
# Num_genes = number of genes
# id = The id of the chromosome
# parent = the parent Id of the chromosome
# recombination = the ID of the chromosome it recombined with.
class chromosome:
    def __init__(self, genes,  id, parent = None, recombination = None):
        self.genes = genes
        self.length = sum([g.length for g in genes])
        self.id = id
        self.parent = parent
        self.recombination = recombination

    # Returns the full chromosome sequence as a string
    # TODO: Complete this
    #
    # Output
    #   Sequence = The full string sequence of the genome as a string
    def sequence_str(self):
        total_sequence = []
        for g in self.genes:
            total_sequence += g.sequence_str()
        return(total_sequence)
    

    # Returns the full chromosome sequence as a string
    # TODO: Complete this
    #
    # Output
    #   Sequence = The full sequence of the genome as a string
    def sequence(self):
        total_sequence = []
        for g in self.genes:
            total_sequence += g.sequence
        return(total_sequence)
    
    #Returns the number of genes in the chromosome.  THis shouldnt change
    def num_genes(self):
        return(len(self.genes))
    
    # This adds a chromsome_id to the recombination tracker list.
    #
    # input:
    #   recombination_chromosome_id = the ID for the chromosome that this one recombined with
    def add_recombination(self, recombination_chromosome_id):
        if self.recombination: #aka if it exists as a list
            self.recombination.append(recombination_chromosome_id)
        elif not self.recombination:
            self.recombination = [recombination_chromosome_id]
        else:
            raise Exception("Recombination is neither something nor None")
    
    
        