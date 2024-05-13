# This holds all common functions for typs of mutations rates CCNV etc.
# Most of these functions are wrappers for Numpy functions such that they play well with my code.

import numpy as np
import random



#This function returns a number rounded to the closest integer about some mean and standard deviation
#
# Input
#   params = Dict {'mean': 5, 'std_dev': .4}
def rounded_norm(params):
    mean = params["mean"]
    std = params["std_dev"]
    return(round(np.random.normal(mean, std)))


# Returns a number from a poisson distribution about some mean
#
# Input
#   param,s = Dict {'mean': Number}
def poisson(params):
    mean = params["mean"]
    return(np.random.poisson(mean))










# This creates point mutations in the Genome with some frequency determiend by the function and function params
# The frequency is on a CELL basis with no BP or cell specific relative frequency of mutations.  The chromosomes
# that have more copies are more likely to see a mutation due to the increased number of copies.  THis is linear.
# Input:
#   cels = List of Cels
#   function = Function determining the frequence of point mutations in a specific cell
#   function_params = List of params for the function above
# Output
#   None
def randomly_distributed_point_mutate_cell(cel, function, function_params):
    number_of_mutation = function(function_params) #This should give the number of mutations
    for i in range(number_of_mutation):
        try:
            # Gets a random chromatid from the chromatids in the cell
            ran_chroma = random.choice(cel.sister_chromatids)

            # Gets a random chromosome from the chromatid
            ran_chromo = random.choice(ran_chroma.chromosomes)
            ran_gene = random.choice(ran_chromo.genes) # Gets a random gene from chromosome
            ran_bp = random.choice(ran_gene.sequence) #Gets a random BP to mutate
        except IndexError:
            print(ran_chromo.length())
            raise Exception("Genes or Sequences have length of Zero.  This cannot be allowed to happen")
        ran_bp.bp = random.choice(dna_functions.bp_options()) #Replaces with a random BP
    return(cel)


# This will randomly mutate the cels in the list cels per the frequencey given by the function and function params
#
# Input:
#   cels = List of Cels
#   function = Function determining the frequence of point mutations in a specific cell
#   function_params = List of params for the function above
# OUtput
#   None
def randomly_distributed_point_mutate_cells(cels, function, function_params):
    return([randomly_distributed_point_mutate_cell(cel, function, function_params) for cel in cels])