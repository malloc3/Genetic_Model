import random
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *


# This is a group of sister chromosomes
#  They are grouped together and can do some funky stuff sometimes
#
# chromosomes = the list of chromosomes that it contains!   They should all be very similar.
class sister_chromosomes:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.length = len(chromosomes)

    # Adds the chromosome to the list of chromosomes and updates the  list!
    def add_chromosome(self, new_chromosome):
        self.chromosomes.append(new_chromosome)
        self.length = len(self.chromosomes)
    
    # Adds a random chromosome from the list of chromosomes and updates list
    def add_random_chromosome(self):
        chromosome_to_duplicate = random.choice(self.chromosomes)
        new_chromosome = self.duplicate_chromosome(chromosome_to_duplicate)
        #TODO THIS ADDS A COPY!  WE WANT A DUPLICATE
        self.add_chromosome(new_chromosome)

    #removes a specific chromosome
    # cchromosome_to_remove = the speciifc chromosome to be removed
    def remove_chromosome(self, chromosome_to_remove):
        self.chromosomes.remove(chromosome_to_remove)
        self.length = len(self.chromosomes)

    # Removes a random chromosome fromthe sister chromosome
    def remove_random_chromosome(self):
        chromosome_to_remove = random.choice(self.chromosomes)
        self.remove_chromosome(chromosome_to_remove)

