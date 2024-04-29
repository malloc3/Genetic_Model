import random
from bp_class import *
from short_DNA_region_class import *

# This is a grouping of genes that creates a chromosome
#
# Each chromosome has some list of genes that make up it's length
class chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.length = len(genes)
