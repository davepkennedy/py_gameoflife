from gol import Board, Cell

from hypothesis import given, settings, Verbosity, example

import hypothesis.strategies as st
import pytest

import random


@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers())
def test_a_cell_with_three_neighbours_spawns(x,y):
    cell = Cell(x,y)
    neighbours = list(cell.neighbours())
    board = Board(neighbours[:3])
    board = board.next_generation()
    assert cell in board.cells

def setup_board_with_cell(cell, neighbour_count):
    neighbours = list(cell.neighbours())
    random.shuffle(neighbours)
    board = Board([cell] + neighbours[:neighbour_count])
    return board.next_generation()

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers(), st.integers(min_value=0,max_value=1))
def test_a_lonely_cell_dies(x,y,count):
    cell = Cell(x,y)
    board = setup_board_with_cell(cell, count)
    assert not cell in board.cells

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers(), st.integers(min_value=2,max_value=3))
def test_a_happy_cell_survives(x,y,count):
    cell = Cell(x,y)
    board = setup_board_with_cell(cell, count)
    assert cell in board.cells

@settings(verbosity=Verbosity.verbose)
@given(st.integers(), st.integers(), st.integers(min_value=4,max_value=8))
def test_an_overcrowded_cell_dies(x,y,count):
    cell = Cell(x,y)
    board = setup_board_with_cell(cell, count)
    assert not cell in board.cells