import random

# This is a class Base Pair.   It only knows its own identity
class Bp:
    def __init__(self, bp):
        self.bp = bp

    
    

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


# This is a grouping of genes that creates a chromosome
#
# Each chromosome has some list of genes that make up it's length
class chromosome:
    def __init__(self, genes):
        self.genes = genes
        self.length = len(genes)


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

