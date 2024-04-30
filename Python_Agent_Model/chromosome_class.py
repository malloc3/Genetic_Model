import random
from bp_class import *
from short_DNA_region_class import *

# This is a grouping of genes that creates a chromosome
#
# Each chromosome has some list of genes that make up it's length
# Length = number of BP
# Num_genes = number of genes
class chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.num_genes = len(genes)
        self.length = sum([g.length for g in genes])

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
    