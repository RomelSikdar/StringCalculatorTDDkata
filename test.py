from TDD import add
import pytest

# This is test for empty string
def test_add_empty_string(): 
    assert add("") == 0

# This is test string "1"
def test_add_single_number(): 
    assert add("1") == 1 

# This is test string "1,2" 1 + 2 = 3
def test_add_two_numbers(): 
    assert add("1,2") == 3 

test_add_empty_string()
test_add_single_number()
test_add_two_numbers()
