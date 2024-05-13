# This holds all common functions for typs of mutations rates CCNV etc.
# Most of these functions are wrappers for Numpy functions such that they play well with my code.

import numpy as np



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


