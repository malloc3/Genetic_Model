import random
from bp_class import *
from short_DNA_region_class import *
from chromosome_class import *
import dna_functions

# This is a group of sister chromosomes
#  They are grouped together and can do some funky stuff sometimes
#
# chromosomes = the list of chromosomes that it contains!   They should all be very similar.
class sister_chromosomes:
    def __init__(self, chromosomes):
        self.chromosomes = chromosomes
        self.num_chromosomes = len(chromosomes)


    # Returns the sequences of the sister chromatids as nested list
    def sequence(self):
        sequences = []
        for chromo in self.chromosomes:
            sequences.append(chromo.sequence())
        return(sequences)
    
    # Returns the sequences string of the sister chromatids as nested list
    def sequence_str(self):
        sequence = []
        for chromo in self.chromosomes:
            sequence.append(chromo.sequence_str())
        return(sequence)
    
    # Returns the length of all the sister chromatids!
    def length_of_chromosomes(self):
        return([chromo.length for chromo in self.chromosomes])
    
    # Adds the chromosome to the list of chromosomes and updates the  list!
    def add_chromosome(self, new_chromosome):
        self.chromosomes.append(new_chromosome)
        self.num_chromosomes = len(self.chromosomes)

    #removes a specific chromosome
    # cchromosome_to_remove = the speciifc chromosome to be removed
    def remove_chromosome(self, chromosome_to_remove):
        if self.num_chromosomes > 1:
            self.chromosomes.remove(chromosome_to_remove)
            self.num_chromosomes = len(self.chromosomes)
        else:
            Warning("Tried to remove a chromosome to less than 1" + id(self))