import math
import os

masses = open('./input.txt','r').readlines()
masses = [ int(m) for m in masses]
def compute_fuel(mass):
    assert type(mass)==int
    return math.floor(mass/3)-2 

def compute_extra_fuel(mass):
    assert type(mass)==int
    extra_fuel = compute_fuel(mass)
    actual_fuel = 0
    while extra_fuel>0:
        actual_fuel+=extra_fuel
        extra_fuel = compute_fuel(extra_fuel)
    return actual_fuel

total_fuel = sum([compute_extra_fuel(m) for m in masses])
print(total_fuel)

