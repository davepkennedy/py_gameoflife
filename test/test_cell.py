from gol import Cell

from hypothesis import given, settings, Verbosity, example

import hypothesis.strategies as st
import pytest

def test_a_cell_neighbours():
    "Testing that a cell has eight neighbours"
    c = Cell(1,1)
    neighbours = set(c.neighbours())
    
    assert Cell(0,0) in neighbours
    assert Cell(0,1) in neighbours
    assert Cell(0,2) in neighbours
    assert Cell(1,0) in neighbours
    assert not Cell(1,1) in neighbours
    assert Cell(1,2) in neighbours
    assert Cell(2,0) in neighbours
    assert Cell(2,1) in neighbours
    assert Cell(2,2) in neighbours
    

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_a_cell_can_be_placed_anywhere(x,y):
    c = Cell(x,y)
    neighbours = set(c.neighbours())

    assert 8 == len(neighbours)