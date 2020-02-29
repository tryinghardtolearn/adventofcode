import os
import day1

def test_compute_fuel():
    assert day1.compute_fuel(1969)==654
    assert day1.compute_fuel(100756)==33583

def test_compute_extra_fuel():
    assert day1.compute_extra_fuel(1969)==966
    assert day1.compute_extra_fuel(100756)==50346
