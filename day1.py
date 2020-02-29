import math
import os

masses = open('./input.txt','r').readlines()
masses = [ int(m) for m in masses]
def compute_fuel(mass):
    assert type(mass)==int
    return math.floor(mass/3)-2 

total_fuel = sum([compute_fuel(m) for m in masses])

print(total_fuel)
