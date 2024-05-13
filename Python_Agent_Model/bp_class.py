import random
from enum import Enum

# Gives the possible options for Base Pairs
def bp_options():
    return(["a", "t", "c", "g"])

# Returns the string value of the baspair.
# Makes it so the code doesn't access the possible strings variable
def bp_string(bp_int_val):
    return(bp_options()[bp_int_val])

# This is a Enum class Base Pair.   It only knows its own identity
class Bp(Enum):
    a = 0
    t = 1
    c = 2
    g = 3

#def __init__(self, bp = "n"):
#    self.bp = bp
