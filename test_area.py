import pytest
import math
from src.area import calculate_area_square

def test_calculate_area_square_negative():
    with pytest.raises(TypeError):
        calculate_area_square(-2)

def test_calculate_area_square_string():
    with pytest.raises(TypeError):
        calculate_area_square("2")

def test_calculate_area_square_list():
    with pytest.raises(TypeError):
        calculate_area_square([2])

# New test case for validating correct area calculation
def test_calculate_area_square_valid():
    side_length = math.sqrt(34)  # Based on your student ID (34)
    expected_area = 34
    assert calculate_area_square(side_length) == expected_area
