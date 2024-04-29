import random
from bp_class import *

# This is a short DNA region.  THis will be a sub class for all the other types of regions
# This includes SNPS, GENES, etc etc
#
# sequence == a list of Bp.   All other attributres will be determied from this
# length == the length of the sequence
class short_DNA_region:
    def __init__(self, sequence):
        self.sequence = sequence
        self.length = len(sequence)



# This is a gene, it is a type of short DNA sequence
# It has an Id since genes are unique.   They also have a lineage
# which is unique.
#
# id = string of numbers and letters for the id of this gene
# lineage = list of strings of the forefathers
class gene(short_DNA_region):
    def __init__(self, sequence):
        super().__init__(sequence)