# This libraary holds helpful functions for dealing with dna!
import random
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *


# This generates a random choice for a base pair
def random_bp():
    bp = random.choice(["a", "c", "g", "t"])
    return(Bp(bp))


# THis duplicates a chromosome with it's genes etc but makes a new exact copy
def duplicate_chromosome(chromosome):
    

